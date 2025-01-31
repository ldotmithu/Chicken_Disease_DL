from pathlib import Path
import os 
from ensure import ensure_annotations
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir:Path = "artifacts/data_ingestion"
    URL:str = 'https://github.com/ldotmithu/Dataset/raw/refs/heads/main/Chicken_Disease.zip'
    local_data_path:Path = "artifacts/data_ingestion/data.zip"
    unzip_dir :Path='artifacts/data_ingestion'
    