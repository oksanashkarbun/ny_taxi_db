import argparse
import os
from time import time
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Ingest Parquet data into PostgreSQL")
    parser.add_argument("--file_path", required=True, help="Path to the Parquet file")
    parser.add_argument("--table_name", required=True, help="Name of the target table")

    args = parser.parse_args()

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST", "pgdatabase")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB")

    if not all([user, password, host, port, db]):
        raise ValueError("❌ Missing database credentials! Check .env file.")

    file_path = args.file_path
    table_name = args.table_name

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    print(f"📂 Loading {file_path} into {table_name}...")

    start = time()
    try:
        table = pq.read_table(file_path)
        df = table.to_pandas()
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"✅ Ingestion completed in {time() - start:.2f} seconds.")
    except Exception as e:
        print(f"❌ Error during ingestion: {e}")

if __name__ == "__main__":
    main()
