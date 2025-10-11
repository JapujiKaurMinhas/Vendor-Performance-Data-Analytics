from sqlalchemy import create_engine
import os
import pandas as pd
import logging
import time

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

from google.colab import drive
drive.mount('/content/drive')

def load_raw_data():
    start = time.time()
    for file in os.listdir('/content/drive/My Drive/Vendor Performence Data Analytics/data'):
        if file.endswith('.csv'): 
            df = pd.read_csv('/content/drive/My Drive/Vendor Performence Data Analytics/data/' + file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, os.path.splitext(file)[0], engine)  # Robust table name
    end = time.time()
    total_time = (end - start) / 60
    logging.info('---------Ingestion Complete--------')
    logging.info(f'Total Time Taken: {total_time} minutes')

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
