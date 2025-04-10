# data_ingestion.py
import pandas as pd

def ingest_data(csv_file):
    try:
        data = pd.read_csv(csv_file)
        return data
    except Exception as e:
        print(f"Error ingesting data: {e}")
        return None