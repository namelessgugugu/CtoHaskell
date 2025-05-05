# Main function.

import os
import sys
import tkinter as tk
# 动态兼容打包后的模块路径
def get_base_dir():
    """获取正确的项目根目录路径（兼容直接运行和 PyInstaller 打包）"""
    if getattr(sys, 'frozen', False):
        # PyInstaller 打包后的环境
        return sys._MEIPASS
    else:
        # 直接运行时，__file__ 是 src/main.py，向上两级到 CtoHaskell 目录
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将项目根目录和 src 目录添加到 Python 路径
BASE_DIR = get_base_dir()
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
# 使用绝对导入（需确保 src/translator 和 src/ui 可以被找到）
from src.translator import Translator  # 从项目根目录导入
from src.ui import TranslatorUI

import tkinter as tk

def main():
    root = tk.Tk()
    translator = Translator()
    app = TranslatorUI(root, translator)
    root.mainloop()

if __name__ == "__main__":
    main()