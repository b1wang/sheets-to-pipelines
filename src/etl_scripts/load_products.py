import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# ----------- ENV ------------
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# ----------- Setup ------------
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

csv_file = "/app/data/products.csv"

create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        sku VARCHAR(50) PRIMARY KEY,
        asin VARCHAR(50)
    )
"""

upsert_query = """
    INSERT INTO products (sku, asin)
    VALUES (:sku, :asin)
    ON CONFLICT (sku)
    DO UPDATE SET asin = EXCLUDED.asin
"""

# ---------- FUNCTIONS ------------
def load_existing_products():
    with engine.connect() as conn:
        return pd.read_sql("SELECT * FROM products", conn)

def create_table():
    with engine.begin() as conn:
        conn.execute(text(create_table_query))

def filter_new_or_changed_records(new_df, existing_df):
    # If the existing DataFrame is empty, treat all new data as inserts
    if existing_df.empty:
        return new_df[['sku', 'asin']]
    
    # Create a dictionary of existing data for faster lookup
    existing_dict = existing_df.set_index('sku')['asin'].to_dict()

    # Filter records where:
    # - SKU is not in the existing data (new record)
    # - or ASIN is different (changed record)
    filtered_df = new_df[
        (new_df['sku'].apply(lambda x: x not in existing_dict)) |
        (new_df['sku'].apply(lambda x: existing_dict.get(x) != new_df.loc[new_df['sku'] == x, 'asin'].values[0]))
    ]

    return filtered_df[['sku', 'asin']]

# ----------- ETL Process ------------

def main():
    create_table()
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip().str.lower()  # Normalize to lowercase
    df = df.drop_duplicates(subset=['sku'])
    df = df.dropna(subset=['sku'])
    print(f"Loaded {len(df)} new records from CSV.")

    existing_df = load_existing_products()
    print(f"Retrieved {len(existing_df)} existing records from database.")

    filtered_df = filter_new_or_changed_records(df, existing_df)
    print(f"{len(filtered_df)} records identified for insert/update.")

    if not filtered_df.empty:
        with engine.begin() as conn:
            for _, row in filtered_df.iterrows():
                conn.execute(text(upsert_query), {"sku": row['sku'], "asin": row['asin']})
            print("Products table updated successfully")

if __name__ == "__main__":
    main()