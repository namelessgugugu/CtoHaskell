from src.loader import load_config, load_prompt
from src.assistant import Assistant, ApiError
from src.translator.checker import CGrammarError, HaskellGrammarError
from src.translator.verifier import Verifier, VerifierError

import pytest

from pathlib import Path

def create_verifier(model):
    secret_path = Path(__file__).parent / "../../config/secret.json"
    api_key = load_config(secret_path)["API_KEY"]

    config_path = Path(__file__).parent / "../../config/general.json"
    config = load_config(config_path)
    assistant = Assistant(
        api_key,
        model,
        0.7,
        10
    )
    gcc_path = config["PATH"]["GCC"]
    ghc_path = config["PATH"]["GHC"]

    system_prompt_path = Path(__file__).parent / "../../prompt/verifier.md"
    system_prompt = load_prompt(system_prompt_path)

    return Verifier(assistant, gcc_path, ghc_path, system_prompt, 3)

def test_verifier_correct():
    verifier = create_verifier("deepseek-ai/DeepSeek-V3")

    c_code_path = Path(__file__).parent / "../data/code/aplusb_in_c.c"
    with open(c_code_path, "r", encoding = "utf-8") as f:
        c_code = f.read()
    
    haskell_code_path = Path(__file__).parent / "../data/code/aplusb_in_haskell.hs"
    with open(haskell_code_path, "r", encoding = "utf-8") as f:
        haskell_code = f.read()
    
    try:
        result = verifier.verify(c_code, haskell_code)
        print(result)
    except VerifierError:
        pass

def test_verifier_fix():
    verifier = create_verifier("deepseek-ai/DeepSeek-V3")

    c_code_path = Path(__file__).parent / "../data/code/prefix.c"
    with open(c_code_path, "r", encoding = "utf-8") as f:
        c_code = f.read()
    
    haskell_code_path = Path(__file__).parent / "../data/code/aplusb_in_haskell.hs"
    with open(haskell_code_path, "r", encoding = "utf-8") as f:
        haskell_code = f.read()
    
    result = verifier.verify(c_code, haskell_code)
    print(result)

def test_optimizer_c_ce():
    verifier = create_verifier("deepseek-ai/DeepSeek-V3")

    c_code_path = Path(__file__).parent / "../data/code/aplusb_in_haskell.hs"
    with open(c_code_path, "r", encoding = "utf-8") as f:
        c_code = f.read()
    
    haskell_code_path = Path(__file__).parent / "../data/code/aplusb_in_haskell.hs"
    with open(haskell_code_path, "r", encoding = "utf-8") as f:
        haskell_code = f.read()
    
    with pytest.raises(CGrammarError):
        verifier.verify(c_code, haskell_code)

def test_optimizer_haskell_ce():
    verifier = create_verifier("deepseek-ai/DeepSeek-V3")

    c_code_path = Path(__file__).parent / "../data/code/aplusb_in_c.c"
    with open(c_code_path, "r", encoding = "utf-8") as f:
        c_code = f.read()
    
    haskell_code_path = Path(__file__).parent / "../data/code/aplusb_in_c.c"
    with open(haskell_code_path, "r", encoding = "utf-8") as f:
        haskell_code = f.read()
    
    with pytest.raises(HaskellGrammarError):
        verifier.verify(c_code, haskell_code)

def test_optimizer_ae():
    verifier = create_verifier("Wrong Model")

    c_code_path = Path(__file__).parent / "../data/code/aplusb_in_c.c"
    with open(c_code_path, "r", encoding = "utf-8") as f:
        c_code = f.read()
    
    haskell_code_path = Path(__file__).parent / "../data/code/aplusb_in_haskell.hs"
    with open(haskell_code_path, "r", encoding = "utf-8") as f:
        haskell_code = f.read()
    
    with pytest.raises(ApiError):
        verifier.verify(c_code, haskell_code)
