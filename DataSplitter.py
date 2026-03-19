import pandas as pd
import math

NUM_PARTS = 10

df = pd.read_csv("Data/Processed/vietnam_processed.csv")

rows_per_part = math.ceil(len(df) / NUM_PARTS)

for i in range(NUM_PARTS):
    part = df.iloc[i * rows_per_part : (i + 1) * rows_per_part]
    part.to_csv(f"data/Processed/vietnam_part_{i+1}.csv", index=False)