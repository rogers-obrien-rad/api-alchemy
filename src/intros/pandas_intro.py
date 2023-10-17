# Introduction to the 'pandas' Library in Python

# --- Package Import ---
# 'pandas' is a powerful library for data analysis and manipulation.
import pandas as pd

# --- Creating a DataFrame ---
# A DataFrame is a 2-dimensional labeled data structure, similar to a table in databases, an Excel sheet, or a data frame in R.
data = {
    'Name': ['John', 'Jane', 'Doe'],
    'Age': [28, 22, 31],
    'City': ['New York', 'Paris', 'London']
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# --- Accessing Data in DataFrame ---
# Using 'loc' to access a row by label/index
print("\nAccessing a row using loc:")
print(df.loc[0])

# Accessing a specific column
print("\nAccessing the 'Name' column:")
print(df['Name'])

# --- Modifying Data ---
# Adding a new column
df['Salary'] = [1000, 1500, 1200]
print("\nDataFrame after adding 'Salary' column:")
print(df)

# Updating a specific value
df.at[1, 'Salary'] = 1600
print("\nDataFrame after updating a salary:")
print(df)

# --- Filtering Data ---
# Filtering rows where 'Age' is greater than 25
filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

# --- Creating DataFrame from JSON Data ---
json_data = [
    {"Name": "Ella", "Age": 25, "City": "Los Angeles"},
    {"Name": "Chris", "Age": 30, "City": "Boston"}
]

df_from_json = pd.DataFrame(json_data)
print("\nDataFrame created from JSON data:")
print(df_from_json)

# --- Saving DataFrames ---
# Saving to CSV
df.to_csv('data.csv', index=False)
print("\nData saved to data.csv!")

# Saving to Excel
df.to_excel('data.xlsx', index=False)
print("Data saved to data.xlsx!")