from chest_disease.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from chest_disease.utils.common import read_yaml, save_json, create_directories
from chest_disease.entity.config_entity import DataIngestionConfig
from pathlib import Path


class ConfigurationManager:
    def __init__(
        self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            unzip_dir=Path(config.unzip_dir),
            workspace=config.workspace,
            project=config.project,
            version=int(config.version),
        )

        return data_ingestion_config
