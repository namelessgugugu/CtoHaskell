# LLM Assistant for generate response.

import requests
import json

class ApiError(RuntimeError):
    def __init__(self, code):
        self.code = code

class Assistant:
    def __init__(self, api_key, model, temperature, retry_limit):
        """
        Create a llm assistant with given model and temperature.

        Parameters:
            api_key - Api key of SiliconFlow.
            model - name of the model to be called.
            temperature - temperature set by the model.
            retry_limit - maximum number of retries if network error occurs.
        """
        self._api_key = api_key
        self._model = model
        self._temperature = temperature
        self._retry_limit = retry_limit
    
    def chat(self, messages):
        """
        Generate a response of given context.

        Parameters:
            messages - a list of previous conversation. Each message
                should follow the format { "role": "user" / "assistant",
                "content": <content>}.
        
        Returns:
            Response generated by llm.

        Raises:
            ApiError(code) - response has an unsuccessful status code, after
                retry_limit retries.
        """
        url = "https://api.siliconflow.cn/v1/chat/completions"
        payload = {
            "model": self._model,
            "messages": messages
        }
        headers = {
            "Authorization": "Bearer " + self._api_key,
            "Content-Type": "application/json"
        }
        for retry in range(self._retry_limit):
            response = requests.request("POST", url, json = payload, headers = headers)
            if response.status_code == 200:
                return json.loads(response.text) \
                    ["choices"] \
                    [0] \
                    ["message"] \
                    ["content"]
            if retry + 1 == self._retry_limit:
                raise ApiError(response.status_code)