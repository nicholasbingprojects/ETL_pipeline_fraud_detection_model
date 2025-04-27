from flask import Flask, request, jsonify
from src.etl.extract import extract
from src.etl.transform import transform
from src.etl.load import load
from src.model.train import train_model
import pandas as pd
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Database connection string
DB_CONNECTION_STRING = 'sqlite:///transactions.db'  

@app.route('/etl', methods=['POST'])
def etl_process():
    # Extract
    data = extract('data/raw/data.csv')
    
    # Transform
    transformed_data = transform(data)
    
    # Load
    load(transformed_data, DB_CONNECTION_STRING)
    
    return jsonify({"message": "ETL process completed successfully!"})

@app.route('/train', methods=['POST'])
def train():
    # Load transformed data
    data = pd.read_sql_table('processed_transactions', con=DB_CONNECTION_STRING)
    
    # Prepare features and target
    X = data[['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']]
    y = data['isFraud']
    
    # Train the model
    model = train_model(X, y)
    
    return jsonify({"message": "Model trained successfully!"})

if __name__ == '__main__':
    app.run(debug=True)