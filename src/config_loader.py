# Load configuration file from director config

from pathlib import Path
import json
from json import JSONDecodeError

def load_config(path):
    """
    Load configuration file with given name.

    Parameters:
        path - path of file (e.g. "../config/general.json" and "../config/secret.json").
    
    Returns:
        A dictionary representing the json file.
    
    Raises:
        FileNotFoundError - File not found.
        JSONDecodeError - File doesn't fit json format.
    """
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)