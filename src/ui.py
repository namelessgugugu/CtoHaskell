import tkinter as tk
from tkinter import ttk, messagebox
from .checker import CGrammarError
from .main import CtoHaskell
class CodeTranslatorUI:
    def __init__(self, master):
        self.master = master
        master.title("C to Haskell Translator")
        # 设置字体
        text_font = ('Courier New', 10)
        
        # 创建主界面布局
        self.create_widgets(text_font)
        
        # 初始化转换器
        self.translator = CtoHaskell()
        # 绑定事件
        self.input_text.bind('<KeyRelease>', self.update_line_numbers)
        self.input_text.bind('<MouseWheel>', self.update_line_numbers)
        self.input_text.bind('<Configure>', self.update_line_numbers)
    def create_widgets(self, text_font):
        # 输入区域
        input_frame = ttk.LabelFrame(self.master, text="C Code Input", padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 创建行号区域
        self.input_line_numbers = tk.Text(
            input_frame, width=4, padx=3, takefocus=0,
            border=0, background='lightgray', state='disabled',
            font=text_font
        )
        self.input_line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        # 主文本框
        self.input_text = tk.Text(
            input_frame, wrap=tk.NONE, font=text_font,
            width=80, height=25
        )
        
        # 滚动条
        input_scroll = ttk.Scrollbar(
            input_frame, orient=tk.VERTICAL,
            command=self.sync_scroll
        )
        self.input_text.configure(yscrollcommand=self.sync_scroll_and_line_numbers)
        
        input_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 转换按钮
        button_frame = ttk.Frame(self.master)
        button_frame.pack(pady=5)
        self.convert_btn = ttk.Button(
            button_frame, text="Convert", command=self.convert
        )
        self.convert_btn.pack(side=tk.LEFT, padx=5)
        # 输出区域 (同样添加行号)
        output_frame = ttk.LabelFrame(self.master, text="Haskell Output", padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.output_line_numbers = tk.Text(
            output_frame, width=4, padx=3, takefocus=0,
            border=0, background='lightgray', state='disabled',
            font=text_font
        )
        self.output_line_numbers.pack(side=tk.LEFT, fill=tk.Y)
        self.output_text = tk.Text(
            output_frame, wrap=tk.NONE, font=text_font,
            width=80, height=25, state=tk.DISABLED
        )
        
        output_scroll = ttk.Scrollbar(
            output_frame, orient=tk.VERTICAL,
            command=self.output_sync_scroll
        )
        self.output_text.configure(yscrollcommand=self.output_sync_scroll_and_line_numbers)
        
        output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 初始化行号
        self.update_line_numbers()
    def sync_scroll(self, *args):
        """同步输入框滚动"""
        self.input_text.yview(*args)
        self.update_line_numbers()
    def sync_scroll_and_line_numbers(self, *args):
        """同步滚动条和行号"""
        self.input_line_numbers.yview(*args)
        self.input_scroll.set(*args)
        self.update_line_numbers()
    def output_sync_scroll(self, *args):
        """同步输出框滚动"""
        self.output_text.yview(*args)
        self.update_output_line_numbers()
    def output_sync_scroll_and_line_numbers(self, *args):
        """同步输出滚动条和行号"""
        self.output_line_numbers.yview(*args)
        self.output_scroll.set(*args)
        self.update_output_line_numbers()
    def update_line_numbers(self, event=None):
        """更新输入框行号"""
        self.update_text_widget_line_numbers(self.input_text, self.input_line_numbers)
    def update_output_line_numbers(self, event=None):
        """更新输出框行号"""
        self.update_text_widget_line_numbers(self.output_text, self.output_line_numbers)
    def update_text_widget_line_numbers(self, text_widget, line_number_widget):
        """通用行号更新方法"""
        # 获取当前可见的行范围
        first, last = text_widget.yview()
        first_line = int(float(first) * float(text_widget.index(tk.END)))
        last_line = int(float(last) * float(text_widget.index(tk.END)))
        # 生成行号文本
        line_numbers_text = "\n".join(
            str(i + 1) for i in range(first_line, last_line)
        )
        
        # 更新行号显示
        line_number_widget.config(state=tk.NORMAL)
        line_number_widget.delete(1.0, tk.END)
        line_number_widget.insert(1.0, line_numbers_text)
        line_number_widget.config(state=tk.DISABLED)
        line_number_widget.yview_moveto(first)
    def convert(self):
        # 获取输入代码
        input_code = self.input_text.get("1.0", tk.END).strip()
        
        if not input_code:
            messagebox.showwarning("Empty Input", "Please enter C code to translate.")
            return
        
        try:
            # 执行转换
            haskell_code = self.translator.run(input_code)
            
            # 显示结果
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, haskell_code)
            self.output_text.config(state=tk.DISABLED)
            
            # 更新输出行号
            self.update_output_line_numbers()
            
        except CGrammarError as e:
            messagebox.showerror("Syntax Error", 
                               f"The input code is not valid C code.\n{e.error_message}")
        except Exception as e:
            messagebox.showerror("Translation Error", 
                               f"Failed to generate Haskell code: {str(e)}")
# def main():
#     root = tk.Tk()
#     app = CodeTranslatorUI(root)
#     root.mainloop()
# if __name__ == "__main__":
#     main()