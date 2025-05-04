# Translate C code to Haskell.

from .checker import HaskellChecker
from .preprocessor import Preprocessor

class TranslateError(RuntimeError):
    def __init__(self):
        pass

class Translator:
    def __init__(
            self,
            assistant,
            gcc_path,
            fake_libc_path,
            ghc_path,
            system_prompt,
            retry_limit
        ):
        """
        Create a translator with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            gcc_path - path of gcc.
            fake_libc_path - path of fake_libc_include.
            ghc_path - path of ghc.
            retry_limit - maximum number of retries if llm generates
                grammatically wrong code.
        """
        self._assistant = assistant
        self._preprocessor = Preprocessor(gcc_path, fake_libc_path)
        self._haskell_checker = HaskellChecker(ghc_path)
        self._system_prompt = system_prompt
        self._retry_limit = retry_limit
    
    def translate(self, code):
        """
        Translate C code to Haskell.

        Parameters:
            code - C code to be translated.
        
        Returns:
            Haskell code.
        
        Raises:
            ApiError(code) - response has an unsuccessful status code, after
                assistant._retry_limit retries.
            CGrammarError - code is not a valid C code.
            ParseError - code cannot be parsed by pycparser.
            TranslateError - llm generates grammatically wrong code,
                after retry_limit retries.
        """
        head_files, global_varibles, other = self._preprocessor.preprocess(code)
        messages = [
            {
                "role": "system",
                "content": self._system_prompt
            },
            {
                "role": "user",
                "content": f"head files:\n{head_files}\n\n" \
                           + f"global varibles:\n{global_varibles}\n\n" \
                           + f"other parts:\n{other}"
            }
        ]

        for _ in range(self._retry_limit):
            reply = self._assistant.chat(messages)

            result = self._haskell_checker.check(reply)
            if result is None:
                return reply
            else:
                messages.append(
                        {
                            "role": "assistant",
                            "content": reply
                        }
                    )
                messages.append(
                        {
                            "role": "user",
                            "content": "Your generation is wrong, here is error message:\n"
                                       + result.error_message
                        }
                    )
        raise TranslateError