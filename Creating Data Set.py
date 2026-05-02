import pandas as pd
import numpy as np

# Read CSV File
df = pd.read_csv("event-versions.csv")

# Repeat rows to reach > 1000
df_1000 = pd.concat([df, df, df], ignore_index = True)

# Randomly generate new event names for all events
df_1000["name"] = [
    f"GW{np.random.randint(15, 26):02d}"
    f"{np.random.randint(1, 13):02d}"
    f"{np.random.randint(1, 29):02d}_"
    f"{np.random.randint(0, 24):02d}"
    f"{np.random.randint(0, 60):02d}"
    f"{np.random.randint(0, 60):02d}"
    for _ in range(len(df_1000))
]

# Rename shortName based on generated name
df_1000["shortName"] = df_1000["name"] + "-v1"

# Keep only first 1000 rows
df_1000 = df_1000.iloc[:1000]

# Save df_1000 as a new CSV
df_1000.to_csv("event-versions_1000.csv", index=False)
