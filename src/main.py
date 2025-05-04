# Main function.

from .translator import Translator
from .ui import TranslatorUI

import tkinter as tk

def main():
    root = tk.Tk()
    translator = Translator()
    app = TranslatorUI(root, translator)
    root.mainloop()

if __name__ == "__main__":
    main()