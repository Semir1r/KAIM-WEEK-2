import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def load_data_from_postgres(query):
    try:
        # Create the connection string
        connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        # Create the engine
        engine = create_engine(connection_string)

        # Load data using pandas read_sql_query
        with engine.connect() as connection:
            df = pd.read_sql_query(query, connection)

        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
