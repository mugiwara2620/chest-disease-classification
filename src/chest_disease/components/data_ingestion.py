import os
from roboflow import Roboflow
from chest_disease.entity.config_entity import DataIngestionConfig
from chest_disease import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """Downloads the dataset directly from Roboflow using the Roboflow Python API."""
        target_dir = str(self.config.unzip_dir)

        if not os.path.exists(target_dir) or len(os.listdir(target_dir)) == 0:
            logger.info("Downloading dataset from Roboflow...")

            # Retrieve API key from environment variables for security
            api_key = os.getenv("ROBOFLOW_API_KEY", "YOUR_ROBOFLOW_API_KEY")

            rf = Roboflow(api_key=api_key)
            project = rf.workspace(self.config.workspace).project(self.config.project)
            dataset = project.version(self.config.version).download(
                "folder", location=target_dir
            )

            logger.info(f"Dataset downloaded successfully to {target_dir}")
        else:
            logger.info("Dataset already exists locally.")
