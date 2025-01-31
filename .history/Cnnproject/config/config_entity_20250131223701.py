from pathlib import Path
import os 
from ensure import ensure_annotations
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir:Path = "artifacts/data_ingestion"
    URL:str = ''