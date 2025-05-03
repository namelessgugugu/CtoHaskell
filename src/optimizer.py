class Optimizer:
    def __init__(self, assistant, retry_limit):
        """
        Create a Optimizer with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            retry_limit - maximum number of retries if llm generates
                grammatically wrong code.
        """
        pass
    
    def optimize(self, code):
        """
        Optimize Haskell code.

        Parameters:
            code - Haskell code to be optimized.
        
        Returns:
            Optimized code.
        
        Raises:
            OptimizeError - llm generates grammatically wrong code,
                after retry_limit retries.
        """
        pass