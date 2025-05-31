from ..assistant import Assistant, ApiError
from .checker import HaskellChecker, CGrammarError
from .preprocessor import ParseError
from .p_translator import PTranslator, PTranslateError
from .agent.optimizer import Optimizer
from .agent.meaning_fixer import MeaningFixer
from .agent.grammar_fixer import GrammarFixer
from .agent import Agent, AgentError

from pathlib import Path

class TranslateError(RuntimeError):
    def __init__(self, error_message):
        self.error_message = error_message

class Translator:
    def __init__(self, configs, prompts):
        """
        Create a translator.
        """
        general_config = configs["GENERAL"]
        secret_config = configs["SECRET"]
        paths = general_config["PATH"]

        gcc_path = paths["GCC"]
        # fake_libc_path = paths["FAKE_LIBC"]
        fake_libc_path = "fake_libc_include"
        ghc_path = paths["GHC"]
        temperature = general_config["TEMPERATURE"]
        model = general_config["MODEL"]
        api_key = secret_config["API_KEY"]
        retry_limit = general_config["RETRY_LIMIT"]

        p_translator_prompt = prompts["P_TRANSLATOR"]
        optimizer_prompt = prompts["OPTIMIZER"]
        meaning_fixer_prompt = prompts["MEANING_FIXER"]
        grammar_fixer_prompt = prompts["GRAMMAR_FIXER"]
        agent_prompt = prompts["AGENT"]

        assistant = Assistant(
            api_key,
            model,
            temperature,
            10
        )

        haskell_checker = HaskellChecker(ghc_path)

        self._p_translator = PTranslator(
            assistant,
            gcc_path,
            fake_libc_path,
            ghc_path,
            p_translator_prompt,
            retry_limit
        )

        grammar_fixer = GrammarFixer(
            haskell_checker,
            assistant,
            grammar_fixer_prompt,
        )

        optimizer = Optimizer(
            assistant,
            optimizer_prompt,
        )

        meaning_fixer = MeaningFixer(
            assistant,
            meaning_fixer_prompt,
        )

        self._agent = Agent(
            assistant,
            agent_prompt,
            haskell_checker,
            grammar_fixer,
            optimizer,
            meaning_fixer,
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
            verified_code = self._agent.run(code, translate_code)
        except ApiError as ae:
            raise TranslateError(f"Fail to call API. Code {ae.code}.")
        except CGrammarError as cge:
            raise TranslateError(f"Invalid input.\n{cge.error_message}")
        except ParseError:
            raise TranslateError("Fail to parse C file.")
        except (PTranslateError, AgentError):
            raise TranslateError("Fail to translate Haskell code.")
        return verified_code
