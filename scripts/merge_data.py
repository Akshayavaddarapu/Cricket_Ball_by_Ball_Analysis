import os
import pandas as pd

# Define the paths
raw_data_path = r"C:\Users\vadda\OneDrive\Documents\Cricket_Ball_by_Ball_Analysis\data\raw"
merged_data_path = r"C:\Users\vadda\OneDrive\Documents\Cricket_Ball_by_Ball_Analysis\data\merged\ipl_merged_deliveries.csv"

# List all CSV files inside "raw" folder
csv_files = [f for f in os.listdir(raw_data_path) if f.endswith(".csv")]

# Create an empty list to store DataFrames
dfs = []

# Read and append each CSV file
for file in csv_files:
    file_path = os.path.join(raw_data_path, file)
    df = pd.read_csv(file_path)
    dfs.append(df)
    print(f"✅ Loaded {file}")

# Merge all DataFrames into one
merged_df = pd.concat(dfs, ignore_index=True)

# Save the merged CSV file
merged_df.to_csv(merged_data_path, index=False)
print(f"\n✅ Merged CSV saved at: {merged_data_path}")
