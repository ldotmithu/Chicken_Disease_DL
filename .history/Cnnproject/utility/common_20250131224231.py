import os 
from Cnnproject import logging

def create_folder(Path):
    try:
        os.makedirs(Path,exist_ok=True)
        logging.info(f'{Path} Folder Created ')
    except Exception as e:
        raise e