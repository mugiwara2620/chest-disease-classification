import os
import yaml
import json
import base64
from pathlib import Path


class ConfigBox(dict):
    """Dictionary subclass that allows attribute-style dot-notation access."""

    def __getattr__(self, key):
        try:
            value = self[key]
            if isinstance(value, dict):
                return ConfigBox(value)
            return value
        except KeyError:
            raise AttributeError(f"'ConfigBox' object has no attribute '{key}'")

    def __setattr__(self, key, value):
        self[key] = value


def read_yaml(path_to_yaml: Path) -> dict:
    """Reads a YAML file and returns a standard dictionary"""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("yaml file is empty")
            return content
    except Exception as e:
        raise e


def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories if they do not exist."""
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)


def save_json(path: Path, data: dict):
    """Saves dictionary data into JSON file."""
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def decodeImage(imgstring, fileName):
    """Decodes a base64 string image and saves it to file."""
    imgdata = base64.b16decode(imgstring)
    with open(fileName, "wb") as f:
        f.write(imgdata)


def encodeImageIntoBase64(croppedImagePath):
    """Encodes a file image into a base64 string."""
    with open(croppedImagePath, "rb") as f:
        return base64.b64decode(f.read())
