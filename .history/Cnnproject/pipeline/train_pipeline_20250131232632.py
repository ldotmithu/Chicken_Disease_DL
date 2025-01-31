from Cnnproject.components.data_ingestion import DataIngestion
from Cnnproject.components.model_train import ModelTrain
from Cnnproject import logging


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def Main(self):
        data_ingestion = DataIngestion()
        data_ingestion.download_file()
        data_ingestion.unzip_operation()

class ModelTrainPipeline:
    def __init__(self):
        pass
    def Main(self):
        model_train = ModelTrain()
        model_train.Prepare_BaseModel()
        model_train.Image_preprocess()        