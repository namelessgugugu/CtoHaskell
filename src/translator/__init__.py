from ..loader import load_config, load_prompt
from ..assistant import Assistant, ApiError
from .checker import CChecker, HaskellChecker, CGrammarError
from .preprocessor import Preprocessor, ParseError
from .p_translator import PTranslator, PTranslateError
from .optimizer import Optimizer, OptimizeError
from .verifier import Verifier, VerifierError

from pathlib import Path

class TranslateError(RuntimeError):
    def __init__(self, error_message):
        self.error_message = error_message

class Translator:
    def __init__(self):
        """
        Create a complete translator.
        """
        from ..loader import load_config
        config = load_config("config/general.json")
        secret = load_config("config/secret.json")
        # config = load_config(Path(__file__).parent / "../../config/general.json")
        # secret = load_config(Path(__file__).parent / "../../config/secret.json")

        gcc_path = config["PATH"]["GCC"]
        fake_libc_path = config["PATH"]["FAKE_LIBC"]
        ghc_path = config["PATH"]["GHC"]
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
