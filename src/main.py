from pathlib import Path
from loader import load_config, load_prompt
from assistant import Assistant
from checker import CChecker, HaskellChecker
from preprocessor import Preprocessor
from translator import Translator
from optimizer import Optimizer
from verifier import Verifier

class CtoHaskell:
    def __init__(self):
        self.config = load_config(Path(__file__).parent / "../config/general.json")
        self.secret = load_config(Path(__file__).parent / "../config/secret.json")
        self.gcc_path = self.config["PATH"]["GCC"]
        self.fake_libc_path = self.config["PATH"]["FAKE_LIBC"]
        self.ghc_path = self.config["PATH"]["GHC"]
        self.retry_limit = self.config["retry_limit"]

        self.assistant = Assistant(
            api_key=self.secret["API_KEY"],
            model=self.config["model"],
            temperature=self.config["temperature"],
            retry_limit=self.retry_limit
        )

        self.translator = Translator(
            assistant=self.assistant,
            gcc_path=self.gcc_path,
            fake_libc_path=self.fake_libc_path,
            ghc_path=self.ghc_path,
            system_prompt=load_prompt(Path(__file__).parent / "prompt" / "translator.md"),
            retry_limit=self.retry_limit
        )

        self.optimizer = Optimizer(
            assistant=self.assistant,
            ghc_path=self.ghc_path,
            system_prompt=load_prompt(Path(__file__).parent / "prompt" / "optimizer.md"),
            retry_limit=self.retry_limit
        )

        self.verifier = Verifier(
            assistant=self.assistant,
            gcc_path=self.gcc_path,
            ghc_path=self.ghc_path,
            system_prompt=load_prompt(Path(__file__).parent / "prompt" / "verifier.md"),
            retry_limit=self.retry_limit
        )
    def run(self, input_code):
        translate_code = self.translator.translate(input_code)
        optimized_code = self.optimizer.optimize(translate_code)
        verified_code = self.verifier.verify(input_code,optimized_code)
        return verified_code

