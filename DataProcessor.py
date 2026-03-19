import pandas as pd

def standardizeData(columns, name, mapping):
    existingMap = {old: new for old, new in mapping.items() if old in columns.columns}
    dStandard = columns[list(existingMap.keys())].copy()

    dStandard = dStandard.rename(columns=existingMap)

    dStandard["war"] = name

    standardNames = [
        "war",
        "mission_id",
        "mission_date",
        "country",
        "aircraft_type",
        "planes",
        "bombload",
        "target_location",
        "target_country",
        "latitude",
        "longitude",
        "weapon_type",
    ]

    for column in standardNames:
        if column not in dStandard.columns:
            dStandard[column] = pd.NA

    dStandard = dStandard[standardNames]

    return dStandard


WW1 = pd.read_csv(
    "Data/Raw/WW1/THOR_WWI_Bombing_Operations.csv",
    encoding="latin-1",
    low_memory=False
)

WW2 = pd.read_csv(
    "Data/Raw/WW2/thor_wwii_data_clean.csv",
    encoding="latin-1",
    low_memory=False
)

koreanWar = pd.read_csv(
    "Data/Raw/Korean_War/THOR_Korean_Bombing_Operations.csv",
    encoding="latin-1",
    low_memory=False
)

vietnamWar = pd.read_csv(
    "Data/Raw/Vietnam_War/THOR_Vietnam_Bombing_Operations.csv",
    encoding="latin-1",
    low_memory=False
)

WW1 = WW1.replace(r'^\s*$', pd.NA, regex=True)
WW2 = WW2.replace(r'^\s*$', pd.NA, regex=True)
koreanWar = koreanWar.replace(r'^\s*$', pd.NA, regex=True)
vietnamWar = vietnamWar.replace(r'^\s*$', pd.NA, regex=True)

WW1Important = [
    "WWI_ID",
    "MSNDATE",
    "COUNTRY",
    "MDS",
    "NUMBEROFPLANESATTACKING",
    "BOMBLOAD",
    "TGTLOCATION",
    "TGTCOUNTRY",
    "LATITUDE",
    "LONGITUDE"
]

WW2Important = [
    "wwii_id",
    "msndate",
    "country_flying_mission",
    "aircraft_name",
    "ac_attacking",
    "total_tons",
    "tgt_location",
    "tgt_country",
    "latitude",
    "longitude"
]

koreanImportant = [
    "KOREAN_ID",
    "MSN_DATE",
    "LAUNCH_COUNTRY",
    "TOTAL_TONS",
]

vietnamImportant = [
    "THOR_DATA_VIET_ID",
    "MSNDATE",
    "COUNTRYFLYINGMISSION",
    "AIRCRAFT_ROOT",
    "NUMOFACFT",
    "WEAPONSLOADEDWEIGHT",
    "TGTCOUNTRY",
    "TGTLATDD_DDD_WGS84",
    "TGTLONDDD_DDD_WGS84"
]

WW1Clean = WW1.drop_duplicates().dropna(subset=WW1Important)
WW2Clean = WW2.drop_duplicates().dropna(subset=WW2Important)
koreanClean = koreanWar.drop_duplicates().dropna(subset=koreanImportant)
vietnamClean = vietnamWar.drop_duplicates().dropna(subset=vietnamImportant)

WW1Map = {
    "WWI_ID": "mission_id",
    "MSNDATE": "mission_date",
    "COUNTRY": "country",
    "MDS": "aircraft_type",
    "NUMBEROFPLANESATTACKING": "planes",
    "BOMBLOAD": "bombload",
    "TGTLOCATION": "target_location",
    "TGTCOUNTRY": "target_country",
    "LATITUDE": "latitude",
    "LONGITUDE": "longitude",
    "WEAPONTYPE": "weapon_type"
}

WW2Map = {
    "wwii_id": "mission_id",
    "msndate": "mission_date",
    "country_flying_mission": "country",
    "aircraft_name": "aircraft_type",
    "ac_attacking": "planes",
    "total_tons": "bombload",
    "tgt_location": "target_location",
    "tgt_country": "target_country",
    "latitude": "latitude",
    "longitude": "longitude"
}

koreanMap = {
    "KOREAN_ID": "mission_id",
    "MSN_DATE": "mission_date",
    "LAUNCH_COUNTRY": "country",
    "AC_TYPE": "aircraft_type",
    "AC_EFFECTIVE": "planes",
    "TOTAL_TONS": "bombload",
}

vietnamMap = {
    "THOR_DATA_VIET_ID": "mission_id",
    "MSNDATE": "mission_date",
    "COUNTRYFLYINGMISSION": "country",
    "AIRCRAFT_ROOT": "aircraft_type",
    "NUMOFACFT": "planes",
    "WEAPONSLOADEDWEIGHT": "bombload",
    "TGTCOUNTRY": "target_country",
    "TGTLATDD_DDD_WGS84": "latitude",
    "TGTLONDDD_DDD_WGS84": "longitude",
    "WEAPONTYPE": "weapon_type"
}

WW1Processed = standardizeData(ww1_clean, "WWI", WW1Map)
WW2Processed = standardizeData(ww2_clean, "WWII", WW2Map)
koreanProcessed = standardizeData(korean_clean, "Korean War", koreanMap)
vietnamProcessed = standardizeData(vietnam_clean, "Vietnam War", vietnamMap)

WW1Processed.to_csv("Data/Processed/ww1_processed.csv", index=False)
WW2Processed.to_csv("Data/Processed/ww2_processed.csv", index=False)
koreanProcessed.to_csv("Data/Processed/korea_processed.csv", index=False)
vietnamprocessed.to_csv("Data/Processed/vietnam_processed.csv", index=False)

print("DONE")