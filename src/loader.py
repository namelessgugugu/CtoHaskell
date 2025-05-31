# Load files.

from pathlib import Path
import json
from json import JSONDecodeError as InvalidJsonError
from pathlib import Path;
import os
import sys

def _get_base_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = Path(__file__).parent.parent
    return str(base_path)

def load_configs(path):
    """
    Load configuration file in given directory path.

    Parameters:
        path - path of config directory (e.g. "../config").
    
    Returns:
        A dictionary representing the json files.
    
    Raises:
        FileNotFoundError - Directory not found.
        InvalidJsonError - Some files do not fit json format.
    """
    result = dict()
    for file_name in os.listdir(path):
        file_path = Path(path) / Path(file_name)
        with open(file_path, "r", encoding = "utf-8") as f:
            content = json.load(f)
        result[str(file_path.stem).upper()] = content
    return result

def load_prompts(path):
    """
    Load prompt text file in given directory path.

    Parameters:
        path - path of prompt directory (e.g. "../prompt")
    
    Returns:
        A string read from file.
    
    Raises:
        FileNotFoundError - File not found.
    """
    result = dict()
    for file_name in os.listdir(path):
        file_path = Path(path) / Path(file_name)
        print(file_path)
        with open(file_path, "r", encoding = "utf-8") as f:
            content = f.read()
        result[str(file_path.stem).upper()] = content
    return result