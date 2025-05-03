from src.config_loader import load_config
from src.checker import CChecker, HaskellChecker, CGrammarError, HaskellGrammarError

import pytest

from pathlib import Path

def test_c_correct():
    config_path = Path(__file__).parent / "../config/general.json"
    gcc_path = load_config(config_path)["PATH"]["GCC"]
    checker = CChecker(gcc_path)

    code_path = Path(__file__).parent / "data/code/aplusb_in_c.c"
    with open(code_path, "r") as f:
        code = f.read()
    assert checker.check(code) is None

def test_c_incorrect():
    config_path = Path(__file__).parent / "../config/general.json"
    gcc_path = load_config(config_path)["PATH"]["GCC"]
    checker = CChecker(gcc_path)

    code_path = Path(__file__).parent / "data/code/aplusb_in_haskell.hs"
    with open(code_path, "r") as f:
        code = f.read()
    
    with pytest.raises(CGrammarError):
        raise checker.check(code)

def test_haskell_correct():
    config_path = Path(__file__).parent / "../config/general.json"
    ghc_path = load_config(config_path)["PATH"]["GHC"]
    checker = HaskellChecker(ghc_path)

    code_path = Path(__file__).parent / "data/code/aplusb_in_haskell.hs"
    with open(code_path, "r") as f:
        code = f.read()
    assert checker.check(code) is None

def test_haskell_incorrect():
    config_path = Path(__file__).parent / "../config/general.json"
    ghc_path = load_config(config_path)["PATH"]["GHC"]
    checker = HaskellChecker(ghc_path)

    code_path = Path(__file__).parent / "data/code/aplusb_in_c.c"
    with open(code_path, "r") as f:
        code = f.read()
    with pytest.raises(HaskellGrammarError):
        raise checker.check(code)
    