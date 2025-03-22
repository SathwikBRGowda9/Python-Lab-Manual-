import pandas as pd

# Load Excel file (ensure the file path is correct)
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Display first 5 rows
print("First 5 rows of data:")
print(df.head())

# Display column names
print("\nColumn Names:")
print(df.columns)

# Get basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Filtering example: Select rows where 'Sales' > 500
filtered_df = df[df["Sales"] > 500]
print("\nFiltered Data (Sales > 500):")
print(filtered_df)

# Save the filtered data to a new Excel file
filtered_df.to_excel("filtered_data.xlsx", index=False)
