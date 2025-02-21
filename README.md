# 🏙️ NY Taxi Database 🚖

---

## **🚀 Getting Started**
### 1️⃣ Clone the repository
```sh
git https://github.com/oksanashkarbun/ny_taxi_db.git
cd ny_taxi_db_project
```

### 2️⃣ Create a .env File
If you need a .env file to store database credentials. Create it in the project root:
```ini
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=ny_taxi
POSTGRES_HOST=pgdatabase
POSTGRES_PORT=5432
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=password
```

## 🛠 Running it
### 3️⃣ Start PostgreSQL and pgAdmin
```sh
docker-compose up -d
```
This starts:
✅ PostgreSQL on localhost:5432
✅ pgAdmin on http://localhost:8080 (Login: admin@admin.com / password)

### 4️⃣ Download Data
```sh
docker-compose run data_processor python download_data.py
```

### 5️⃣ Ingest Data into PostgreSQL
```shell
docker-compose run data_processor python ingest_data.py
```
Verify tables exist:
```shell
docker-compose run data_processor psql -h pgdatabase -U user -d ny_taxi -c "\dt"
```

## 🖥️ Accessing the Database
### 🔹 pgAdmin (GUI)
1. Open http://localhost:8080.
2. Login: admin@admin.com / password
3. Add new Server () 
4. Connection tab data:
 - Host: pgdatabase
 - Port: 5432
 - Username: user
 - Password: password

### 🔹 Direct Access with psql
```shell
docker-compose run data_processor psql -h pgdatabase -U user -d ny_taxi
```
### ✅ Verifying Data
```sql
SELECT COUNT(*) FROM <table_name>;
SELECT * FROM <table_name> LIMIT 5;
```
### Cleaning Up
To stop all containers:
```shell
docker-compose down
```
To remove all data (WARNING: This deletes all data):
```shell
docker-compose down --volumes
```
