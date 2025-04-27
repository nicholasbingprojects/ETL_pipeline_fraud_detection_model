import pandas as pd
from src.etl.extract import extract
from src.etl.transform import transform
from src.etl.load import load

def test_etl():
    raw_data = extract('data/raw/data.csv')
    transformed_data = transform(raw_data)
    load(transformed_data, 'data/processed/transformed_data.csv')
    
    processed_data = pd.read_csv('data/processed/transformed_data.csv')
    assert not processed_data.empty