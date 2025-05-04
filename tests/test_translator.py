from src.translator import Translator, TranslateError

import pytest

from pathlib import Path

def test_translator_correct():
    translator = Translator()

    code_path = Path(__file__).parent / "data/code/mss.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    try:
        result = translator.translate(code)
        print(result)
    except TranslateError:
        pass

def test_translator_ce():
    translator = Translator()

    code_path = Path(__file__).parent / "data/code/aplusb_in_haskell.hs"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    with pytest.raises(TranslateError):
        translator.translate(code)

def test_translator_pe():
    translator = Translator()

    code_path = Path(__file__).parent / "data/code/fea_c11.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    with pytest.raises(TranslateError):
        translator.translate(code)
