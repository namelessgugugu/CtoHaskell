# Fix gammar error of Haskell code.

class GrammarFixer:
    def __init__(self, haskell_checker, assistant, system_prompt):
        """
        Create a Grammarfixer with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            system_prompt - system prompt of GrammarFixer.
        """
        self._haskell_checker = haskell_checker
        self._assistant = assistant
        self._system_prompt = system_prompt
    
    def grammar_fix(self, haskell_code, compilation_information):
        """
        Modify Haskell code to fix grammar errors.

        Parameters:
            haskell_code - Haskell code.
        
        Returns:
            Modified haskell code.
        
        Raises:
            ApiError(code) - response has an unsuccessful status code, after
                assistant._retry_limit retries.
        """
        if self._haskell_checker.check(haskell_code) == None:
            return haskell_code
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
        return self._assistant.chat(messages)