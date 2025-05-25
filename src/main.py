# Main function.

from .translator import Translator
from .ui import TranslatorUI
from .loader import load_configs, load_prompts
from pathlib import Path

import tkinter as tk

def main():
    root = tk.Tk()
    config_path = Path(__file__).parent / "../config"
    prompt_path = Path(__file__).parent / "../prompt"
    configs = load_configs(config_path)
    prompts = load_prompts(prompt_path)
    translator = Translator(configs, prompts)
    app = TranslatorUI(root, translator)
    root.mainloop()

if __name__ == "__main__":
    main()