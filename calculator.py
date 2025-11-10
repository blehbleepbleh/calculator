#create a calculator GUI with basic operations: addition, subtraction, multiplication, and division and use tkinter
#have buttons with digits 0-9, operations +, -, *, /, = and C (clear)
"""Calculator GUI using Tkinter"""
import tkinter as tk
from tkinter import messagebox
class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('330x460')
        self.resizable(False, False)
        self.expression = ''
        self._build_ui()

    def _build_ui(self):
        pad = 8
        frm = tk.Frame(self, padx=pad, pady=pad)
        frm.pack(fill=tk.BOTH, expand=True)

        self.display = tk.Entry(frm, font=('Segoe UI', 18), borderwidth=2, relief='ridge', justify='right')
        self.display.pack(fill=tk.BOTH, pady=(0, 10))

        btn_frame = tk.Frame(frm)
        btn_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(btn_frame, text=text, font=('Segoe UI', 14), width=5, height=2,
                            command=lambda t=text: self._on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

    def _on_button_click(self, char):
        if char == 'C':
            self.expression = ''
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ''
                self.display.delete(0, tk.END)
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
def main():
    app = CalculatorApp()
    app.mainloop()


if __name__ == '__main__':
    main()