import os
import time
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# PostgreSQL credentials
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "pgdatabase")
port = os.getenv("POSTGRES_PORT", "5432")
db = os.getenv("POSTGRES_DB")

if not all([user, password, host, port, db]):
    raise ValueError("❌ Missing database credentials! Check .env file.")

# Database connection
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

# Define data folder inside Docker
DATA_FOLDER = "/data"

# Set the chunk size (number of rows per batch)
CHUNK_SIZE = 100_000  # Adjust as needed for performance


def ingest_parquet(file_path):
    table_name = os.path.splitext(os.path.basename(file_path))[0]  # Use filename as table name
    print(f"📂 Processing {file_path} into table `{table_name}` in chunks...")

    start_time = time.time()
    try:
        parquet_file = pq.ParquetFile(file_path)
        total_rows = parquet_file.metadata.num_rows
        print(f"🔹 File `{file_path}` contains {total_rows} rows.")

        first_chunk = True  # Track whether this is the first chunk

        # Read and insert in chunks
        for batch in parquet_file.iter_batches(batch_size=CHUNK_SIZE):
            df_chunk = batch.to_pandas()

            # Insert into PostgreSQL
            df_chunk.to_sql(table_name, engine, if_exists="replace" if first_chunk else "append", index=False)
            first_chunk = False

            print(f"✅ {len(df_chunk)} rows inserted into `{table_name}`.")

        print(f"🎉 `{file_path}` fully ingested into `{table_name}` in {time.time() - start_time:.2f} seconds.")

    except Exception as e:
        print(f"❌ Error ingesting `{file_path}`: {e}")


# Ingest all .parquet files in /data
if os.path.exists(DATA_FOLDER):
    parquet_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".parquet")]

    if parquet_files:
        print(f"\n🔎 Found {len(parquet_files)} Parquet files for ingestion: {parquet_files}\n")
        for file in parquet_files:
            ingest_parquet(os.path.join(DATA_FOLDER, file))
    else:
        print("⚠️ No Parquet files found in `/data/`.")
else:
    print("❌ `/data/` directory does not exist.")
