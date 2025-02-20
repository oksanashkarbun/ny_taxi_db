import os
from time import time
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")
    table_name = os.getenv("TABLE_NAME")

    file_path = "data/dataset1.parquet"  # Modify this as needed

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Read parquet file
    file = pq.ParquetFile(file_path)
    df_iter = file.iter_batches(batch_size=100000)

    # Create table schema
    df = next(df_iter).to_pandas()
    df.to_sql(name=table_name, con=engine, if_exists='replace')

    while True:
        try:
            t_start = time()
            batch = next(df_iter).to_pandas()
            batch.to_sql(name=table_name, con=engine, if_exists='append')
            print(f'Inserted another chunk in {time() - t_start:.3f} seconds')
        except StopIteration:
            print('Finished ingesting data into PostgreSQL')
            break

if __name__ == '__main__':
    main()
