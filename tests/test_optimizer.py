from src.loader import load_config, load_prompt
from src.assistant import Assistant
from src.checker import HaskellGrammarError
from src.optimizer import Optimizer, OptimizeError

import pytest

from pathlib import Path

def create_optimizer():
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
    ghc_path = config["PATH"]["GHC"]

    system_prompt_path = Path(__file__).parent / "../prompt/optimizer.md"
    system_prompt = load_prompt(system_prompt_path)

    return Optimizer(assistant, ghc_path, system_prompt, 3)

def test_optimizer_correct():
    optimizer = create_optimizer()

    code_path = Path(__file__).parent / "data/code/prefix.hs"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    try:
        result = optimizer.optimize(code)
        print(result)
    except OptimizeError:
        pass

def test_optimizer_ce():
    optimizer = create_optimizer()

    code_path = Path(__file__).parent / "data/code/aplusb_in_c.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    
    with pytest.raises(HaskellGrammarError):
        optimizer.optimize(code)
