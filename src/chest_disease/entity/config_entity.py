from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    unzip_dir: Path
    workspace: str
    project: str
    version: int


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: str
    imge_size: list
    learning_rate: float
    classes: int
