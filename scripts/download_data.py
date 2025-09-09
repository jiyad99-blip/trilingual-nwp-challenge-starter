#!/usr/bin/env python3
"""
Data download script for trilingual neural weather prediction challenge.

This script downloads the required datasets for the competition including:
- Weather forecast data in English, French, and German
- Historical weather observations
- Evaluation datasets
"""

import os
import urllib.request
import zipfile
from pathlib import Path

def download_file(url: str, filename: str) -> None:
    """Download a file from URL to local path."""
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded {filename}")

def extract_zip(zip_path: str, extract_to: str) -> None:
    """Extract a zip file to specified directory."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")

def main():
    """Main download function."""
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Placeholder URLs - replace with actual competition data URLs
    datasets = {
        "training_data.zip": "https://example.com/training_data.zip",
        "test_data.zip": "https://example.com/test_data.zip",
        "weather_vocab.json": "https://example.com/weather_vocab.json"
    }
    
    # Download datasets
    for filename, url in datasets.items():
        filepath = data_dir / filename
        if not filepath.exists():
            try:
                download_file(url, str(filepath))
                # Extract zip files
                if filename.endswith('.zip'):
                    extract_zip(str(filepath), str(data_dir))
            except Exception as e:
                print(f"Error downloading {filename}: {e}")
                print("Please check the URL and try again.")
        else:
            print(f"{filename} already exists, skipping download.")
    
    print("Data download complete!")

if __name__ == "__main__":
    main()
