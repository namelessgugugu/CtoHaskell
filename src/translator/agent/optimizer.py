# Optimize Haskell code.

class Optimizer:
    def __init__(self, assistant, system_prompt):
        """
        Create a Optimizer with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            system_prompt - system prompt of Optimizer.
        """
        self._assistant = assistant
        self._system_prompt = system_prompt
    
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
        return self._assistant.chat(messages)