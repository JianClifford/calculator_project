import tkinter as tk
from calculator.operations import add, subtract, multiply, divide

class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")

        self.screen = tk.Entry(self.root, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.screen.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        self.create_buttons()

    def create_buttons(self):
        row = 1
        col = 0
        for button in self.buttons:
            b = tk.Button(self.root, text=button, padx=20, pady=20, font=("Arial", 18))
            b.grid(row=row, column=col)
            b.bind("<Button-1>", self.click)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = str(eval(self.screen.get()))
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, result)
            except Exception as e:
                self.screen.delete(0, tk.END)
                self.screen.insert(tk.END, "Error")
        elif text == "C":
            self.screen.delete(0, tk.END)
        else:
            self.screen.insert(tk.END, text)

    def run(self):
        self.root.mainloop()