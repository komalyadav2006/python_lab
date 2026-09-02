import pandas as pd

# Read CSV file
file_name = input("Enter CSV file name: ")

df = pd.read_csv(file_name)

# Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Display dimensions
print("\nDataset Dimensions:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Select column for filtering
column = input("\nEnter column name for filtering: ")
value = float(input("Enter value: "))

# Filter rows
filtered_data = df[df[column] > value]

print("\nFiltered Data:")
print(filtered_data)

# Export filtered data
output_file = "cleaned_data.csv"
filtered_data.to_csv(output_file, index=False)

print("\nFiltered data successfully saved to:", output_file)