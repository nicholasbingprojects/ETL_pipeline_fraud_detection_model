import pandas as pd

def transform(data):
    """Transform the data (e.g., cleaning, feature engineering)."""
    # Example transformation: drop null values and reset index
    transformed_data = data.dropna().reset_index(drop=True)
    
    # Add any additional transformations here
    # Example: transformed_data['new_feature'] = transformed_data['existing_feature'] * 2

    return transformed_data

def main():
    # Assuming data has been extracted and is available as 'data'
    file_path = 'data/raw/data.csv'  # Path to raw data
    data = pd.read_csv(file_path)
    
    transformed_data = transform(data)
    
    # Save the transformed data
    transformed_data.to_csv('data/processed/transformed_data.csv', index=False)
    print("Transformed data saved to 'data/processed/transformed_data.csv'")

if __name__ == "__main__":
    main()