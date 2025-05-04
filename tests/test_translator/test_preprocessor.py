from src.loader import load_config
from src.translator.checker import CGrammarError
from src.translator.preprocessor import Preprocessor, ParseError

import pytest

from pathlib import Path

def create_preprocessor():
    config_path = Path(__file__).parent / "../../config/general.json"
    gcc_path = load_config(config_path)["PATH"]["GCC"]
    fake_libc_path = load_config(config_path)["PATH"]["FAKE_LIBC"]
    return Preprocessor(gcc_path, fake_libc_path)

def test_preprocessor_correct():
    preprocessor = create_preprocessor()

    code_path = Path(__file__).parent / "../data/code/aplusb_in_c.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    head_file, global_varibles, other = preprocessor.preprocess(code)
    assert head_file == ["stdio.h", "string.h"]
    assert global_varibles == ["int a = 0", "int b = 1"]
    assert other == "int main(void)\n{\n  scanf(\"%d%d\", &a, &b);\n  printf(\"%d\\n\", a + b);\n  return 0;\n}"

def test_preprocessor_ce():
    preprocessor = create_preprocessor()

    code_path = Path(__file__).parent / "../data/code/aplusb_in_haskell.hs"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    with pytest.raises(CGrammarError):
        preprocessor.preprocess(code)

def test_preprocessor_pe():
    preprocessor = create_preprocessor()

    code_path = Path(__file__).parent / "../data/code/fea_c11.c"
    with open(code_path, "r", encoding = "utf-8") as f:
        code = f.read()
    with pytest.raises(ParseError):
        preprocessor.preprocess(code)