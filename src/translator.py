class Translator:
    def __init__(self, assistant, retry_limit):
        """
        Create a translator with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            retry_limit - maximum number of retries if llm generates
                grammatically wrong code.
        """
        pass
    
    def translate(self, code):
        """
        Translate C code to Haskell.

        Parameters:
            code - C code to be translated.
        
        Returns:
            Haskell code.
        
        Raises:
            TranslateError - llm generates grammatically wrong code,
                after retry_limit retries.
        """
        pass