from src.loader import load_configs
from src.translator.checker import CChecker, HaskellChecker, CGrammarError, HaskellGrammarError

import pytest

from pathlib import Path

def create_c_checker():
    config_path = Path(__file__).parent / "../../config"
    gcc_path = load_configs(config_path)["GENERAL"]["PATH"]["GCC"]
    return CChecker(gcc_path)

def test_c_correct():
    checker = create_c_checker()

    code_path = Path(__file__).parent / "../data/code/aplusb_in_c.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    assert checker.check(code) is None

def test_c_incorrect():
    checker = create_c_checker()

    code_path = Path(__file__).parent / "../data/code/aplusb_in_haskell.hs"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    with pytest.raises(CGrammarError):
        raise checker.check(code)

def create_haskell_checker():
    config_path = Path(__file__).parent / "../../config"
    ghc_path = load_configs(config_path)["GENERAL"]["PATH"]["GHC"]
    return HaskellChecker(ghc_path)

def test_haskell_correct():
    checker = create_haskell_checker()

    code_path = Path(__file__).parent / "../data/code/aplusb_in_haskell.hs"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    assert checker.check(code) is None

def test_haskell_incorrect():
    checker = create_haskell_checker()
    
    code_path = Path(__file__).parent / "../data/code/aplusb_in_c.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    with pytest.raises(HaskellGrammarError):
        raise checker.check(code)
    