from src.config_loader import load_config, JSONDecodeError

import pytest

from pathlib import Path

def test_config_load_pass():
    path = Path(__file__).parent / "data/config/correct.json"
    load_config(path)

def test_config_load_not_found():
    path = Path(__file__).parent / "data/config/not_found.json"
    with pytest.raises(FileNotFoundError):
        load_config(path)

def test_config_load_invalid_format():
    path = Path(__file__).parent / "data/config/incorrect.json"
    with pytest.raises(JSONDecodeError):
        load_config(path)