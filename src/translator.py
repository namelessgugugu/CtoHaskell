from checker import HaskellChecker

class Translator:
    def __init__(self, assistant, retry_limit):
        """
        Create a translator with given assistant.

        Parameters:
            assistant - an Assistant from assistant.py.
            retry_limit - maximum number of retries if llm generates
                grammatically wrong code.
        """
        self.assistant = assistant
        self.retry_limit = retry_limit
        self.checker = HaskellChecker()
    
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
        for i in range(self.retry_limit):
            print(f"[Translator] Attempt {i + 1} to translate...")

            messages = [
                {
                    "role": "system",
                    "content": (
                        "你是一个将 C 语言代码转换为 Haskell 的助手。"
                        "请用 Idiomatic Haskell 代码保留 C 语言代码原始功能。"
                    )
                },
                {
                    "role": "user",
                    "content": f"请将下面的 C 语言代码翻译成 Haskell：\n{code}"
                }
            ]

            try:
                reply = self.assistant.chat(messages)
            except Exception as error:
                print(f"[Translator] Assistant error: {error}")
                continue

            error_message = self.checker.check(reply)
            if error_message is None:
                print("[Translator] Translation passed syntax check.")
                return reply
            else:
                print(f"[Translator] Translated Haskell code failed syntax check: {error_message}")
                print("[Translator] Retrying translation...")

        print("[Translator] Translation failed after retries.")
        return None