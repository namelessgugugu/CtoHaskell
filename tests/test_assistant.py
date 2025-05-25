from src.loader import load_configs
from src.assistant import Assistant, ApiError

import pytest

from pathlib import Path

def test_assistant_correct():
    path = Path(__file__).parent / "../config"
    api_key = load_configs(path)["SECRET"]["API_KEY"]
    assistant = Assistant(
        api_key,
        "deepseek-ai/DeepSeek-V3",
        0.7,
        10
    )
    assistant.chat([{"role": "user", "content": "Introduce yourself"}])


def test_assistant_invalid():
    path = Path(__file__).parent / "../config"
    api_key = load_configs(path)["SECRET"]["API_KEY"]
    assistant = Assistant(
        api_key,
        "deepseek-ai/DeepSeek-V3",
        0.7,
        10
    )
    with pytest.raises(ApiError):
        assistant.chat([{"role111": "use222r", "co123ntent": "Intro   duce yourself"}])