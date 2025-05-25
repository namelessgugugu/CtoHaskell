from src.loader import load_configs, load_prompts, InvalidJsonError

import pytest

from pathlib import Path

def test_config_load_pass():
    path = Path(__file__).parent / "data/correct_config"
    load_configs(path)

def test_config_load_not_found():
    path = Path(__file__).parent / "data/not_found_config"
    with pytest.raises(FileNotFoundError):
        load_configs(path)

def test_config_load_invalid_format():
    path = Path(__file__).parent / "data/incorrect_config"
    with pytest.raises(InvalidJsonError):
        load_configs(path)

def test_prompt_load_pass():
    path = Path(__file__).parent / "data/correct_config"
    load_prompts(path)

def test_prompt_load_not_found():
    path = Path(__file__).parent / "data/not_found_config"
    with pytest.raises(FileNotFoundError):
        load_prompts(path)