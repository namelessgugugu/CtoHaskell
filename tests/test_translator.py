from src.loader import load_config, load_prompt
from src.assistant import Assistant
from src.checker import CGrammarError
from src.preprocessor import ParseError
from src.translator import Translator, TranslateError

import pytest

from pathlib import Path

def create_translator():
    secret_path = Path(__file__).parent / "../config/secret.json"
    api_key = load_config(secret_path)["API_KEY"]

    config_path = Path(__file__).parent / "../config/general.json"
    config = load_config(config_path)
    assistant = Assistant(
        api_key,
        "deepseek-ai/DeepSeek-R1",
        0.7,
        10
    )
    gcc_path = config["PATH"]["GCC"]
    fake_libc_path = config["PATH"]["FAKE_LIBC"]
    ghc_path = config["PATH"]["GHC"]

    system_prompt_path = Path(__file__).parent / "../prompt/translator.md"
    system_prompt = load_prompt(system_prompt_path)

    return Translator(assistant, gcc_path, fake_libc_path, ghc_path, system_prompt, 3)

def test_translator_correct():
    translator = create_translator()

    code_path = Path(__file__).parent / "data/code/prefix.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    try:
        result = translator.translate(code)
        print(result)
    except TranslateError:
        pass

def test_translator_ce():
    translator = create_translator()

    code_path = Path(__file__).parent / "data/code/aplusb_in_haskell.hs"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    with pytest.raises(CGrammarError):
        translator.translate(code)

def test_translator_pe():
    translator = create_translator()

    code_path = Path(__file__).parent / "data/code/fea_c11.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    with pytest.raises(ParseError):
        translator.translate(code)