# Verify whether C code and Haskell code are the same.

from .checker import CChecker, HaskellChecker

class MeaningfixError(RuntimeError):
    def __init__(self):
        pass

class Meaningfixer:
    def __init__(self, assistant, gcc_path, ghc_path, system_prompt, retry_limit):
        """
        Create a Verifiers with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            retry_limit - maximum number of retries if llm generates
                grammatically wrong code.
        """
        self._assistant = assistant
        self._c_checker = CChecker(gcc_path)
        self._haskell_checker = HaskellChecker(ghc_path)
        self._system_prompt = system_prompt
        self._retry_limit = retry_limit
    
    def meaning_fix(self, c_code, haskell_code):
        """
        Verify whether c_code and haskell_code are the same.

        Parameters:
            c_code - C code.
            haskell_code - Haskell code.
        
        Returns:
            Modified haskell code, which equals to original haskell_code
            if it's correct.
        
        Raises:
            ApiError(code) - response has an unsuccessful status code, after
                assistant._retry_limit retries.
            CGrammarError - c_code is not a valid C code.
            HaskellGrammarError - haskell_code is not a valid C code.
            VerifyError - llm generates grammatically wrong code,
                after retry_limit retries.
        """
        c_check_result = self._c_checker.check(c_code)
        if c_check_result is not None:
            raise c_check_result
        haskell_check_result = self._haskell_checker.check(haskell_code)
        if haskell_check_result is not None:
            raise haskell_check_result
        
        messages = [
            {
                "role": "system",
                "content": self._system_prompt
            },
            {
                "role": "user",
                "content": f"C code:\n{c_code}\n\nHaskell code:\n{haskell_code}\n"
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
        raise MeaningfixError