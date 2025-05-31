# Main function.

import os
import sys
from pathlib import Path
import tkinter as tk
def get_base_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = get_base_dir()
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
from src.translator import Translator
from src.ui import TranslatorUI
from src.loader import load_configs, load_prompts

def find_config_path(filename="config"):
    search_paths = [
        Path(sys.executable).parent / filename,

        Path(__file__).parent / filename,
        
        Path(__file__).parent.parent / filename,

        Path(__file__).parent.parent.parent / filename,
        
        # 3. 直接当前目录（简易用法）
        Path.cwd(),
    ]
    
    for path in search_paths:
        if path.exists():
            print (str(path))
            return str(path)
    
    raise FileNotFoundError(f"{filename} not found in: {[str(p) for p in search_paths]}")


def main():
    root = tk.Tk()
    config_path = find_config_path()
    # config_path = Path(__file__).parent.parent / "config"
    if getattr(sys, 'frozen', False):
        prompt_path = Path(sys._MEIPASS) / "prompt"
    else:
        prompt_path = Path(__file__).parent.parent / "prompt"
    # prompt_path = Path(__file__).parent.parent / "prompt"
    print(prompt_path)
    configs = load_configs(config_path)
    prompts = load_prompts(prompt_path)
    translator = Translator(configs, prompts)
    app = TranslatorUI(root, translator)
    root.mainloop()

if __name__ == "__main__":
    main()