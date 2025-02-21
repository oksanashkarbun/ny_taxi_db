import os

# Define the folder to save data (Inside Docker)
DATA_FOLDER = "/data"

# Ensure the /data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Dictionary of dataset file names and their corresponding Google Drive file IDs
file_links = {
    "dataset1.parquet": "1wf927g6729o93m3U1UkYortXR5PhBV7p",
    "dataset2.parquet": "1c-l3X6AunESLBd0SzqUkPYEha4_TcrMH",
    "dataset3.parquet": "1Q78fBVm91ZZctW6fvDA3BEHFf4_KSHbN",
    "dataset4.parquet": "13O7u9IBoFC1Lb7i3K6sGGaSd8GzqFsCQ",
    "dataset5.parquet": "1S9cWmUgJLsWSCz8Tm1GxAZjSDT7I7DIx",
    "dataset6.parquet": "1iFDzzHPx7KfQoGzIVTGn_uvpQBAR6185",
    "dataset7.parquet": "1bgOzcZcQ6evOCnny3WW2WI76yFyi-369",
    "dataset8.parquet": "1E9V2LbnEgPDeran7-Bn7HwlmibLRPYW3",
    "dataset9.parquet": "1CnTvw6InqO1EhR_nYZsalEAX1ZUquQ83",
    "dataset10.parquet": "1Gb9GPSkyWmmG4qyMZXr3wANVcnLCUmqc",
    "dataset11.parquet": "1u82XQVjF7mK_oAni-bdOminm5r6rOPwP",
}

def download_file(filename, file_id):
    output_path = os.path.join(DATA_FOLDER, filename)
    print(f"📥 Downloading {filename} to {output_path}...")

    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    exit_code = os.system(f"wget --no-check-certificate '{url}' -O {output_path}")

    # Check if the download was successful
    if exit_code == 0:
        print(f"✅ {filename} downloaded successfully and saved to {output_path}!")
    else:
        print(f"❌ Failed to download {filename}. Check Google Drive access.")

# Loop through and download all files with original names
for file_name, file_id in file_links.items():
    download_file(file_name, file_id)

# Verify files exist after download
print("\n📂 Verifying downloaded files in /data/")
os.system("ls -lh /data")

print("\n🎉 All files downloaded successfully!")
