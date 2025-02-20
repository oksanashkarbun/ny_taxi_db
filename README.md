# NY Taxi Database 

## 🚀 Getting Started

### 1️⃣ Clone the repository
```sh
git clone https://github.com/yourusername/ny_taxi_db_project.git
cd ny_taxi_db_project
```

### 2️⃣Install dependencies
```sh
pip install -r requirements.txt
```
##### How to Get the Data
```sh
python download_data.py
```
Check the `data/` folder for downloaded files.


### 3️⃣ Start the PostgreSQL database
```sh
docker-compose up -d
```

### 4️⃣ Run the data ingestion script
```sh
python ingest_data.py --user user --password password --host localhost --port 5432 --db ny_taxi --table_name taxi_data --url <DATASET_URL>
```

### 5️⃣ Access pgAdmin
Open: http://localhost:8080
Login: admin@admin.com / password




