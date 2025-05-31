# Fix Haskell code to match C code.

class MeaningFixer:
    def __init__(self, assistant, system_prompt):
        """
        Create a MeaningFixer with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            system_prompt - system prompt of MeaningFixer
        """
        self._assistant = assistant
        self._system_prompt = system_prompt
    
    def meaning_fix(self, c_code, haskell_code):
        """
        Fix haskell_code to match c_code.

        Parameters:
            c_code - C code.
            haskell_code - Haskell code.
        
        Returns:
            Modified haskell code.
        
        Raises:
            ApiError(code) - response has an unsuccessful status code, after
                assistant._retry_limit retries.
        """
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
        reply = self._assistant.chat(messages)
        if reply == "PASS":
            return haskell_code
        return reply