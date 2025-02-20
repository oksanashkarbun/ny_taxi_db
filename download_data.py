import os
import gdown
from dotenv import load_dotenv

load_dotenv()

DATA_FOLDER = os.getenv("DATA_FOLDER", "data")
GDRIVE_FOLDER_URL = os.getenv("GDRIVE_FOLDER_URL")

file_links = {
    "dataset1.parquet": "https://drive.google.com/file/d/1wf927g6729o93m3U1UkYortXR5PhBV7p/view?usp=sharing",
    "dataset2.parquet": "https://drive.google.com/file/d/1c-l3X6AunESLBd0SzqUkPYEha4_TcrMH/view?usp=sharing",
    "dataset3.parquet": "https://drive.google.com/file/d/1Q78fBVm91ZZctW6fvDA3BEHFf4_KSHbN/view?usp=sharing",
    "dataset4.parquet": "https://drive.google.com/file/d/13O7u9IBoFC1Lb7i3K6sGGaSd8GzqFsCQ/view?usp=sharing",
    "dataset5.parquet": "https://drive.google.com/file/d/1S9cWmUgJLsWSCz8Tm1GxAZjSDT7I7DIx/view?usp=sharing",
    "dataset6.parquet": "https://drive.google.com/file/d/1iFDzzHPx7KfQoGzIVTGn_uvpQBAR6185/view?usp=sharing",
    "dataset7.parquet": "https://drive.google.com/file/d/1bgOzcZcQ6evOCnny3WW2WI76yFyi-369/view?usp=sharing",
    "dataset8.parquet": "https://drive.google.com/file/d/1E9V2LbnEgPDeran7-Bn7HwlmibLRPYW3/view?usp=drive_link",
    "dataset9.parquet": "https://drive.google.com/file/d/1CnTvw6InqO1EhR_nYZsalEAX1ZUquQ83/view?usp=sharing",
    "dataset10.parquet": "https://drive.google.com/file/d/1Gb9GPSkyWmmG4qyMZXr3wANVcnLCUmqc/view?usp=sharing",
    "dataset11.parquet": "https://drive.google.com/file/d/1u82XQVjF7mK_oAni-bdOminm5r6rOPwP/view?usp=drive_link",
}

# Create the data directory if it doesn't exist
os.makedirs(DATA_FOLDER, exist_ok=True)

# Download each file
for file_name, file_url in file_links.items():
    output_path = os.path.join(DATA_FOLDER, file_name)
    print(f"Downloading {file_name} to {output_path}...")
    gdown.download(file_url, output_path, quiet=False)

print("✅ All files downloaded successfully!")
