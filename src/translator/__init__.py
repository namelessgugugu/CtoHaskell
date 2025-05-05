from ..loader import load_config, load_prompt
from ..assistant import Assistant, ApiError
from .checker import CChecker, HaskellChecker, CGrammarError
from .preprocessor import Preprocessor, ParseError
from .p_translator import PTranslator, PTranslateError
from .optimizer import Optimizer, OptimizeError
from .verifier import Verifier, VerifierError

import sys
import os
from pathlib import Path

class TranslateError(RuntimeError):
    def __init__(self, error_message):
        self.error_message = error_message

def find_config_path(filename="general.json"):
    """智能查找配置文件路径（优先外部文件）"""
    search_paths = [
        # 1. 优先找EXE同级目录下的config文件夹（适用于打包后）
        Path(sys.executable).parent / "config" / filename,
        
        # 2. 开发环境路径（适用于调试）
        Path(__file__).parent.parent / "config" / filename,

        Path(__file__).parent.parent.parent / "config" / filename,
        
        # 3. 直接当前目录（简易用法）
        Path.cwd() / filename,
    ]
    
    for path in search_paths:
        if path.exists():
            print (str(path))
            return str(path)
    
    raise FileNotFoundError(f"{filename} not found in: {[str(p) for p in search_paths]}")


class Translator:
    def __init__(self):
        """
        Create a complete translator.
        """
        from ..loader import load_config
        config = load_config(find_config_path("general.json"))
        secret = load_config(find_config_path("secret.json"))
        # config = load_config("config/general.json")
        # secret = load_config("config/secret.json")
        # config = load_config(Path(__file__).parent / "../../config/general.json")
        # secret = load_config(Path(__file__).parent / "../../config/secret.json")

        gcc_path = config["PATH"]["GCC"]
        print(gcc_path)
        fake_libc_path = config["PATH"]["FAKE_LIBC"]
        ghc_path = config["PATH"]["GHC"]
        print(ghc_path)
        temperature = config["TEMPERATURE"]
        model = config["MODEL"]
        api_key = secret["API_KEY"]
        retry_limit = config["RETRY_LIMIT"]

        assistant = Assistant(
            api_key,
            model,
            temperature,
            retry_limit
        )

        p_translator_prompt = load_prompt(Path(__file__).parent / "../../prompt/p_translator.md")
        optimizer_prompt = load_prompt(Path(__file__).parent / "../../prompt/optimizer.md")
        verifier_prompt = load_prompt(Path(__file__).parent / "../../prompt/verifier.md")

        self._p_translator = PTranslator(
            assistant,
            gcc_path,
            fake_libc_path,
            ghc_path,
            p_translator_prompt,
            retry_limit
        )

        self._optimizer = Optimizer(
            assistant,
            ghc_path,
            optimizer_prompt,
            retry_limit
        )

        self._verifier = Verifier(
            assistant,
            gcc_path,
            ghc_path,
            verifier_prompt,
            retry_limit
        )
    def translate(self, code):
        """
        Translate C to Haskell.

        Parameters:
            code - C code.

        Returns:
            Haskell code.
        
        Raises:
            TranslateError - Fail to translate code.
        """
        try:
            translate_code = self._p_translator.translate(code)
            optimized_code = self._optimizer.optimize(translate_code)
            verified_code = self._verifier.verify(code, optimized_code)
        except ApiError as ae:
            raise TranslateError(f"Fail to call API. Code {ae.code}.")
        except CGrammarError as cge:
            raise TranslateError(f"Invalid input.\n{cge.error_message}")
        except ParseError:
            raise TranslateError("Fail to parse C file.")
        except (PTranslateError, OptimizeError, VerifierError):
            raise TranslateError("Fail to translate Haskell code.")
        return verified_code
