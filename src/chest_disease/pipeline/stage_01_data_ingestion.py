import sys
from pathlib import Path

# Add project root and src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from chest_disease.config.configuration import ConfigurationManager
from chest_disease.components.data_ingestion import DataIngestion

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()


if __name__ == "__main__":
    try:
        print(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        print(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise e
