from src.translator import Translator, TranslateError
from src.loader import load_configs, load_prompts

import pytest

from pathlib import Path

def test_translator_correct():
    
    config_path = Path(__file__).parent / "../config"
    configs = load_configs(config_path)
    prompt_path = Path(__file__).parent / "../prompt"
    prompts = load_prompts(prompt_path)

    translator = Translator(configs, prompts)

    code_path = Path(__file__).parent / "data/code/aplusb_in_c.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    try:
        result = translator.translate(code)
        print(result)
    except TranslateError:
        pass

def test_translator_ce():

    config_path = Path(__file__).parent / "../config"
    configs = load_configs(config_path)
    prompt_path = Path(__file__).parent / "../prompt"
    prompts = load_prompts(prompt_path)

    translator = Translator(configs, prompts)

    code_path = Path(__file__).parent / "data/code/aplusb_in_haskell.hs"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    with pytest.raises(TranslateError):
        translator.translate(code)

def test_translator_pe():

    config_path = Path(__file__).parent / "../config"
    configs = load_configs(config_path)
    prompt_path = Path(__file__).parent / "../prompt"
    prompts = load_prompts(prompt_path)

    translator = Translator(configs, prompts)

    code_path = Path(__file__).parent / "data/code/fea_c11.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    with pytest.raises(TranslateError):
        translator.translate(code)
