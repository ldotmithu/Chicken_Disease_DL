from Cnnproject.components.data_ingestion import DataIngestion
from Cnnproject import logging


class DataIngestionPipeline(self):
    def __init__(self):
        pass
    
    def Main(self):
        data_ingestion = DataIngestion()
        data_ingestion.download_file()
        data_ingestion.unzip_operation()