import os
import gdown
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the folder to save data
DATA_FOLDER = os.getenv("DATA_FOLDER", "data")

# Ensure the data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Dictionary of dataset file names and their Google Drive file IDs
file_links = {
    "dataset1.parquet": "1wf927g6729o93m3U1UkYortXR5PhBV7p",
    # "dataset2.parquet": "1c-l3X6AunESLBd0SzqUkPYEha4_TcrMH",
    # "dataset3.parquet": "1Q78fBVm91ZZctW6fvDA3BEHFf4_KSHbN",
    # "dataset4.parquet": "13O7u9IBoFC1Lb7i3K6sGGaSd8GzqFsCQ",
    # "dataset5.parquet": "1S9cWmUgJLsWSCz8Tm1GxAZjSDT7I7DIx",
    # "dataset6.parquet": "1iFDzzHPx7KfQoGzIVTGn_uvpQBAR6185",
    # "dataset7.parquet": "1bgOzcZcQ6evOCnny3WW2WI76yFyi-369",
    # "dataset8.parquet": "1E9V2LbnEgPDeran7-Bn7HwlmibLRPYW3",
    # "dataset9.parquet": "1CnTvw6InqO1EhR_nYZsalEAX1ZUquQ83",
    # "dataset10.parquet": "1Gb9GPSkyWmmG4qyMZXr3wANVcnLCUmqc",
    # "dataset11.parquet": "1u82XQVjF7mK_oAni-bdOminm5r6rOPwP",
}

def download_file(filename, file_id):
    """Downloads a file from Google Drive using gdown with fuzzy matching."""
    output_path = os.path.join(DATA_FOLDER, filename)
    print(f"📥 Downloading {filename}...")

    # Use correct URL format
    url = f"https://drive.google.com/uc?id={file_id}"

    # Use fuzzy=True to auto-correct Google Drive URLs
    gdown.download(url, output_path, quiet=False, fuzzy=True)

# Download all files
for file_name, file_id in file_links.items():
    download_file(file_name, file_id)

print("✅ All files downloaded successfully!")
