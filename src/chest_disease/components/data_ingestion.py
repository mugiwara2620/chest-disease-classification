import os
from pathlib import Path
from roboflow import Roboflow
from chest_disease.entity.config_entity import DataIngestionConfig
from chest_disease import logger


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Resolve path as an absolute path string
        target_dir = str(Path(self.config.unzip_dir).resolve())
        os.makedirs(target_dir, exist_ok=True)

        logger.info(f"Target dataset directory: {target_dir}")

        api_key = os.getenv("ROBOFLOW_API_KEY")
        if not api_key:
            raise ValueError("ROBOFLOW_API_KEY environment variable is missing!")

        rf = Roboflow(api_key=api_key)
        project = rf.workspace(self.config.workspace).project(self.config.project)

        # Download dataset
        version = project.version(self.config.version)
        dataset = version.download(model_format="folder", location=target_dir)

        logger.info(f"Dataset successfully downloaded to: {dataset.location}")
