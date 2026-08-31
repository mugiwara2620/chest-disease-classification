import os
import zipfile
import gdown
from chest_disease.entity.config_entity import DataIngestionConfig
from chest_disease import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """Downloads dataset zip file from source URL."""
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading data from {self.config.source_URL}")
            gdown.download(
                self.config.source_URL, str(self.config.local_data_file), quiet=False
            )
            logger.info(f"Downloaded data to {self.config.local_data_file}")
        else:
            logger.info("Dataset file already exists.")

    def extract_zip_file(self):
        """Extracts the downloaded zip file to the target artifacts directory."""
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted dataset to {unzip_path}")
