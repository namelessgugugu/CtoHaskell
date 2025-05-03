class Verifier:
    def __init__(self, assistant, retry_limit):
        """
        Create a Verifiers with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            retry_limit - maximum number of retries if llm generates
                grammatically wrong code.
        """
        pass
    
    def verify(self, c_code, haskell_code):
        """
        Verify whether c_code and haskell_code are the same.

        Parameters:
            c_code - C code.
            haskell_code - Haskell code.
        
        Returns:
            Modified haskell code, which equals to original haskell_code
            if it's correct.
        
        Raises:
            VerifyError - llm generates grammatically wrong code,
                after retry_limit retries.
        """
        pass