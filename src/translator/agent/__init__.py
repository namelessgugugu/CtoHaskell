from ..checker import HaskellChecker

class TranslateError(RuntimeError):
    def __init__(self, error_message):
        self.error_message = error_message

class Agent:
    def __init__(self, assistant, system_prompt, ghc_path, grammar_fixer, optimizer, meaning_fixer, retry_limit):
        """
        Create an AI agent.
        """
        self._assistant = assistant
        self._system_prompt = system_prompt
        self._haskell_checker = HaskellChecker(ghc_path)
        self._grammar_fixer = grammar_fixer
        self._optimizer = optimizer
        self._meaning_fixer = meaning_fixer
        self._retry_limit = retry_limit

    def run(self, C_code, Haskell_code):
        """
        Translate C to Haskell.

        Parameters:
            code - C code.

        Returns:
            Haskell code.
        
        Raises:
            TranslateError - Fail to translate code.
        """
        
        self.C_code = C_code
        self.Haskell_code = Haskell_code
        messages = [
            {
                "role": "system",
                "content": self._system_prompt
            }
        ]
        for _ in range(self._retry_limit):
            
            result = self._haskell_checker.check(self.Haskell_code)
            if result is None: 
                self.compilation_information = "Pass compilation."
            else:
                self.compilation_information = "Your code failed to compile, here is error message:\n"
                + result.error_message
            messages.append(
                {
                    "role": "user",
                    "content": f"C_code:\n{self.C_code}\n\n" \
                           + f"Haskell_code:\n{self.Haskell_code}\n\n" \
                           + f"compilation_information:\n{self.compilation_information}"
                }
            )
            # `grammer_fix`, `optimize`, `meaning_fix`, `pass`
            reply = self._assistant.chat(messages)
            messages.append(
                {
                    "role": "assistant",
                    "content": reply
                }
            )
            print(f"Debug: now={_},{reply}")
            if reply == "pass":
                return self.Haskell_code
            elif reply == "grammer_fix":
                self.Haskell_code = self._grammar_fixer.grammar_fix(self.Haskell_code,self.compilation_information)
            elif reply == "optimize":
                self.Haskell_code = self._optimizer.optimize(self.Haskell_code)
            elif reply == "meaning_fix":
                self.Haskell_code = self._meaning_fixer.meaning_fix(self.C_code,self.Haskell_code)
            else:
                continue
        return self.Haskell_code
