# Load files.

import os
import sys
from pathlib import Path
import json
from json import JSONDecodeError as InvalidJsonError
def _get_base_path():
    """动态获取项目根目录（兼容开发和打包环境）"""
    if getattr(sys, 'frozen', False):
        # 打包后：从 _MEIPASS 根目录开始查找（PyInstaller 临时文件夹）
        base_path = sys._MEIPASS
    else:
        # 开发环境：从当前文件所在目录回溯到项目根目录
        base_path = Path(__file__).parent.parent
    return str(base_path)

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
    full_path = os.path.join(_get_base_path(), path)

    with open(full_path, 'r', encoding = 'utf-8') as f:
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
    full_path = os.path.join(_get_base_path(), path)
    with open(full_path, "r", encoding = "utf-8") as f:
        return f.read()