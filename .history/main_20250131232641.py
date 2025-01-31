from Cnnproject.pipeline.train_pipeline import DataIngestionPipeline,ModelTrainPipeline
from Cnnproject import logging

try:
    logging.info(">>>>>DataIngestion>>>>>>")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.Main()
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>')
except Exception as e:
    raise e