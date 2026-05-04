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
