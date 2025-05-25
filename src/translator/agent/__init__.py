class AgentError(RuntimeError):
    def __init__(self):
        pass

class Agent:
    def __init__(
            self,
            assistant,
            system_prompt,
            haskell_checker,
            grammar_fixer,
            optimizer,
            meaning_fixer,
            retry_limit
        ):
        """
        Create an AI agent.
        """
        self._assistant = assistant
        self._system_prompt = system_prompt
        self._haskell_checker = haskell_checker
        self._grammar_fixer = grammar_fixer
        self._optimizer = optimizer
        self._meaning_fixer = meaning_fixer
        self._retry_limit = retry_limit

    def run(self, c_code, haskell_code):
        """
        Translate C to Haskell.

        Parameters:
            code - C code.

        Returns:
            Haskell code.
        
        Raises:
            AgentError - agent didn't call PASS after retry_limit retries.
        """
        
        messages = [
            {
                "role": "system",
                "content": self._system_prompt
            }
        ]
        for _ in range(self._retry_limit):
            
            result = self._haskell_checker.check(haskell_code)
            if result is None: 
                compilation_information = "Pass compilation."
            else:
                compilation_information = f"Your code raises compilition errors. Message:\n{result.error_message}"
            messages.append(
                {
                    "role": "user",
                    "content": f"C_code:\n{c_code}\n\n" \
                           + f"Haskell_code:\n{haskell_code}\n\n" \
                           + f"compilation_information:\n{compilation_information}"
                }
            )
            reply = self._assistant.chat(messages)
            messages.append(
                {
                    "role": "assistant",
                    "content": reply
                }
            )
            print(f"Debug: now={_},{reply},{haskell_code}")
            if reply == "pass":
                return haskell_code
            elif reply == "grammar_fix":
                haskell_code = self._grammar_fixer.grammar_fix(haskell_code, compilation_information)
            elif reply == "optimize":
                haskell_code = self._optimizer.optimize(haskell_code)
            elif reply == "meaning_fix":
                haskell_code = self._meaning_fixer.meaning_fix(c_code, haskell_code)
            else:
                continue
        raise AgentError
