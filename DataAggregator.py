import pandas as pd
import json
import os

ww1 = pd.read_csv("Data/Processed/ww1_processed.csv", low_memory=False)
ww2 = pd.read_csv("Data/Processed/ww2_processed.csv", low_memory=False)
korea = pd.read_csv("Data/Processed/korea_processed.csv", low_memory=False)

vietnam_parts = []
for i in range(1, 11):
    path = f"Data/Processed/vietnam_part_{i}.csv"
    if os.path.exists(path):
        vietnam_parts.append(pd.read_csv(path, low_memory=False))
        print(f"Loaded {path}")
vietnam = pd.concat(vietnam_parts, ignore_index=True)

print(f"WW1: {len(ww1)} rows")
print(f"WW2: {len(ww2)} rows")
print(f"Korea: {len(korea)} rows")
print(f"Vietnam: {len(vietnam)} rows")

all_data = pd.concat([ww1, ww2, korea, vietnam], ignore_index=True)

def parse_dates(df):
    df["mission_date"] = pd.to_datetime(df["mission_date"], format="mixed", dayfirst=False, errors="coerce")
    df["year"] = df["mission_date"].dt.year
    df["month"] = df["mission_date"].dt.to_period("M").astype(str)
    return df

all_data = parse_dates(all_data)

future_mask = all_data["mission_date"].dt.year > 2025
all_data.loc[future_mask, "mission_date"] -= pd.DateOffset(years=100)
all_data["year"] = all_data["mission_date"].dt.year
all_data["month"] = all_data["mission_date"].dt.to_period("M").astype(str)

all_data["bombload"] = pd.to_numeric(all_data["bombload"], errors="coerce").fillna(0)
all_data["planes"] = pd.to_numeric(all_data["planes"], errors="coerce").fillna(0)
all_data["latitude"] = pd.to_numeric(all_data["latitude"], errors="coerce")
all_data["longitude"] = pd.to_numeric(all_data["longitude"], errors="coerce")

os.makedirs("data", exist_ok=True)


timeline = (
    all_data.groupby(["war", "month"])
    .agg(missions=("mission_id", "count"), bombload=("bombload", "sum"))
    .reset_index()
)
timeline = timeline.dropna(subset=["month"])
timeline = timeline[timeline["month"] != "NaT"]
timeline.to_json("data/timeline.json", orient="records")
print(f"timeline.json: {len(timeline)} rows")


map_data = all_data.dropna(subset=["latitude", "longitude"]).copy()
map_data["lat_round"] = (map_data["latitude"] * 2).round() / 2
map_data["lon_round"] = (map_data["longitude"] * 2).round() / 2

map_agg = (
    map_data.groupby(["war", "lat_round", "lon_round"])
    .agg(missions=("mission_id", "count"), bombload=("bombload", "sum"))
    .reset_index()
)
map_agg = map_agg.rename(columns={"lat_round": "lat", "lon_round": "lon"})
map_agg.to_json("data/map_data.json", orient="records")
print(f"map_data.json: {len(map_agg)} rows")


stats = (
    all_data.groupby("war")
    .agg(
        total_missions=("mission_id", "count"),
        total_bombload=("bombload", "sum"),
        total_planes=("planes", "sum"),
        countries=("country", "nunique"),
        target_countries=("target_country", "nunique"),
        start_date=("mission_date", "min"),
        end_date=("mission_date", "max"),
    )
    .reset_index()
)
stats["start_date"] = stats["start_date"].astype(str)
stats["end_date"] = stats["end_date"].astype(str)
stats_dict = stats.to_dict(orient="records")

with open("data/stats.json", "w") as f:
    json.dump(stats_dict, f, indent=2)
print(f"stats.json: {len(stats_dict)} wars")


top_targets = (
    all_data.dropna(subset=["target_location"])
    .groupby(["war", "target_location", "target_country"])
    .agg(missions=("mission_id", "count"), bombload=("bombload", "sum"))
    .reset_index()
    .sort_values(["war", "missions"], ascending=[True, False])
)
top_per_war = top_targets.groupby("war").head(20)
top_per_war.to_json("data/top_targets.json", orient="records")
print(f"top_targets.json: {len(top_per_war)} rows")


by_country = (
    all_data.groupby(["war", "country"])
    .agg(missions=("mission_id", "count"), bombload=("bombload", "sum"))
    .reset_index()
    .sort_values(["war", "missions"], ascending=[True, False])
)
by_country.to_json("data/by_country.json", orient="records")
print(f"by_country.json: {len(by_country)} rows")


by_aircraft = (
    all_data.dropna(subset=["aircraft_type"])
    .groupby(["war", "aircraft_type"])
    .agg(missions=("mission_id", "count"), bombload=("bombload", "sum"))
    .reset_index()
    .sort_values(["war", "missions"], ascending=[True, False])
)
top_aircraft = by_aircraft.groupby("war").head(15)
top_aircraft.to_json("data/top_aircraft.json", orient="records")
print(f"top_aircraft.json: {len(top_aircraft)} rows")

