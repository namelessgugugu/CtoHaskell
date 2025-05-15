# Verify whether C code and Haskell code are the same.

from .checker import HaskellChecker

class GrammarfixError(RuntimeError):
    def __init__(self):
        pass

class Grammarfixer:
    def __init__(self, assistant, ghc_path, system_prompt, retry_limit):
        """
        Create a Grammarfixer with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            retry_limit - maximum number of retries if llm generates
                grammatically wrong code.
        """
        self._assistant = assistant
        self._haskell_checker = HaskellChecker(ghc_path)
        self._system_prompt = system_prompt
        self._retry_limit = retry_limit
    
    def grammar_fix(self, haskell_code, compilation_information):
        """
        Modify Haskell code until it passes compilation.

        Parameters:
            haskell_code - Haskell code.
        
        Returns:
            Modified haskell code, which passes compilation.
        
        Raises:
            ApiError(code) - response has an unsuccessful status code, after
                assistant._retry_limit retries.
            GrammarfixError - llm generates grammatically wrong code,
                after retry_limit retries.
        """
        
        messages = [
            {
                "role": "system",
                "content": self._system_prompt
            },
            {
                "role": "user",
                "content": f"Haskell code:\n{haskell_code}\n\ncompilation_information:\n{compilation_information}\n"
            }
        ]
        for _ in range(self._retry_limit):
            reply = self._assistant.chat(messages)

            if reply == "PASS":
                return haskell_code

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
        raise GrammarfixError