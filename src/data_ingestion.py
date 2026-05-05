import os 
import kagglehub
import shutil
from src.logger import get_logger
from src.custom_exeption import CustomExeption
from config.data_ingestion_config import *
import zipfile
import sys

logger = get_logger(__name__)


class DataIngestion:
    def __init__(self,dataset_name:sys,target_dir:sys):
        self.dataset_name=dataset_name
        self.target_dir=target_dir

    def data_ingestion(self):
        raw_dir = os.path.join(TARGET_DIR,"raw")
        
        if not os.path.exists(raw_dir):
            try:
                os.makedirs(raw_dir,exist_ok=True)
                logger.info(f"Directory created: {raw_dir}")
                
            except Exception as e:
                logger.error("Data ingestin is wrong...!")
                raise CustomExeption("Error while data ingestion.",e)
