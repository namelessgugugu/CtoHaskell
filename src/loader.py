# Load files.

from pathlib import Path
import json
from json import JSONDecodeError as InvalidJsonError

def load_config(path):
    """
    Load configuration file with given path.

    Parameters:
        path - path of file (e.g. "../config/general.json" and "../config/secret.json").
    
    Returns:
        A dictionary representing the json file.
    
    Raises:
        FileNotFoundError - File not found.
        InvalidJsonError - File doesn't fit json format.
    """
    with open(path, 'r', encoding = 'utf-8') as f:
        return json.load(f)

def load_prompt(path):
    """
    Load prompt text file with given path.

    Parameters:
        path - path of file (e.g. "../prompt/translator")
    
    Returns:
        A string read from file.
    
    Raises:
        FileNotFoundError - File not found.
    """
    with open(path, "r", encoding = "utf-8") as f:
        return f.read()