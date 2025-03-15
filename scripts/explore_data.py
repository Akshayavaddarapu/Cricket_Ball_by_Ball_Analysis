import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\vadda\OneDrive\Documents\Cricket_Ball_by_Ball_Analysis\data\merged\ipl_merged_deliveries.csv")  # Replace with your actual file path

# Convert 'date' column to datetime format and handle missing values
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['date'].fillna(df['date'].mode()[0], inplace=True)  # Filling missing dates with the most common date

# Convert numerical columns to appropriate types, handling missing values
numeric_cols = ['innings', 'over', 'runs_of_bat', 'extras', 'wide', 'legbyes', 'byes', 'noballs']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
df[numeric_cols] = df[numeric_cols].fillna(0)  # Filling NaN values with 0 for numerical columns

# Convert 'innings' and 'over' to integers (Fix the innings and over columns)
df["innings"] = df["innings"].astype("int")
df["over"] = df["over"].astype("int")

# Handling NaN Values for categorical columns
df.fillna("Unknown", inplace=True)  # Replace missing values with "Unknown"

# Display first 5 rows
print("Data loaded successfully!\n")
print("First 5 rows:\n", df.head())

# Display dataset info
print("\nDataset Info:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))
