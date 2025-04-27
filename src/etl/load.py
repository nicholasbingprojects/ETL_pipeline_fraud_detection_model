import pandas as pd
from sqlalchemy import create_engine
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def load_to_db_and_csv(host, user, password, database, table_name, csv_path):
    """Load the transformed data into a MySQL database and save it to CSV."""
    try:
        # Create SQLAlchemy engine with a timeout
        engine = create_engine(
            f'mysql+mysqlconnector://{user}:{password}@{host}/{database}',
            connect_args={'connect_timeout': 2}  # Set timeout for connection
        )
        
        connection = engine.connect()  # Create a connection
        transaction = connection.begin()  # Start a transaction
        
        # Read the transformed data
        data = pd.read_csv(csv_path)
        
        # Load the data into a specified table
        data.to_sql(name=table_name, con=connection, if_exists='replace', index=False)
        logging.info(f"Data loaded into table '{table_name}' in the database '{database}'")
        
        # Save the data to the CSV file (optional)
        data.to_csv(csv_path, index=False)
        logging.info(f"Data saved to '{csv_path}'")
        
        transaction.commit()  # Commit the transaction only if all operations succeeded
    
    except Exception as e:
        logging.error(f"Error: {e}")
        transaction.rollback()  # Rollback the transaction in case of error
    
    finally:
        if 'transaction' in locals() and transaction.is_active:
            transaction.rollback()  # Ensure rollback in case of failure
        if 'connection' in locals() and connection:
            connection.close()  # Ensure the connection is closed
            logging.info("Connection closed. Operation completed.")

def main():
    # Database connection parameters
    host = os.getenv('DB_HOST', 'localhost')             
    user = os.getenv('DB_USER', 'root')                   
    password = os.getenv('DB_PASSWORD', '')              
    database = os.getenv('DB_NAME', 'transaction_db')     
    table_name = 'transformed_data'                      
    csv_path = 'data/processed/transformed_data.csv'    

    load_to_db_and_csv(host, user, password, database, table_name, csv_path)

if __name__ == "__main__":
    main()