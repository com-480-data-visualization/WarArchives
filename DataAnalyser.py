import pandas as pd

WW1 = pd.read_csv("Data/Processed/ww1_processed.csv")
WW2 = pd.read_csv("Data/Processed/ww2_processed.csv")
korea = pd.read_csv("Data/Processed/korea_processed.csv")

vietnamDivs = []
for i in range(1, 11):
    part = pd.read_csv(f"Data/Processed/vietnam_part_{i}.csv")
    vietnamDivs.append(part)

vietnam = pd.concat(vietnamDivs, ignore_index=True)

datasets = {
    "WWI": WW1,
    "WWII": WW2,
    "Korean War": korea,
    "Vietnam War": vietnam
}

output = ""

for war_name, df in datasets.items():
    df["mission_date"] = pd.to_datetime(df["mission_date"], errors="coerce")
    df["year"] = df["mission_date"].dt.year

    output += f"\n=== {war_name} ===\n"
    output += f"Total missions: {len(df)}\n"

    if df["year"].notna().any():
        output += f"Year range: {int(df['year'].min())} - {int(df['year'].max())}\n"

    if "bombload" in df.columns:
        output += f"Average bombload: {df['bombload'].mean():.2f}\n"
        output += f"Total bombload: {df['bombload'].sum():.2f}\n"

    if "planes" in df.columns:
        output += f"Average planes attacking: {df['planes'].mean():.2f}\n"
        output += f"Total planes attacking: {df['planes'].sum():.2f}\n"

with open("Data/Processed/basic_stats.txt", "w", encoding="utf-8") as f:
    f.write(output)

print("Basic statistics written to Data/Processed/basic_stats.txt")