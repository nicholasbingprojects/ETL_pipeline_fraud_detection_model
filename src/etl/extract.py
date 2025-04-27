import pandas as pd
import os

def extract(file_path):
    """Extract data from a CSV file."""
    return pd.read_csv(file_path)

# Specify the actual file path for raw data
file_path = 'data/raw/data.csv'  # Adjust as necessary based on your current working directory

# Print current working directory for debugging
print("Current working directory:", os.getcwd())

# Call the extract function
try:
    data = extract(file_path)
    print(data.head())  # Print the first few rows of the data
except FileNotFoundError as e:
    print(f"Error: {e}. Please check the file path.")