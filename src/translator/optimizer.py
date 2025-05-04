# Optimize Haskell code.

from .checker import HaskellChecker

class OptimizeError(RuntimeError):
    def __init__(self):
        pass

class Optimizer:
    def __init__(self, assistant, ghc_path, system_prompt, retry_limit):
        """
        Create a Optimizer with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            ghc_path - path of ghc.
            system_prompt - prompt to guide llm.
            retry_limit - maximum number of retries if llm generates
                grammatically wrong code.
        """
        self._assistant = assistant
        self._haskell_checker = HaskellChecker(ghc_path)
        self._system_prompt = system_prompt
        self._retry_limit = retry_limit
    
    def optimize(self, code):
        """
        Optimize Haskell code.

        Parameters:
            code - Haskell code to be optimized.
        
        Returns:
            Optimized code.
        
        Raises:
            HaskellGrammarError - code is not valid haskell code.
            OptimizeError - llm generates grammatically wrong code,
                after retry_limit retries.
        """
        check_result = self._haskell_checker.check(code)
        if check_result is not None:
            raise check_result
        messages = [
            {
                "role": "system",
                "content": self._system_prompt
            },
            {
                "role": "user",
                "content": code
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
        raise OptimizeError