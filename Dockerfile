FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y wget postgresql-client

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "download_data.py"]
