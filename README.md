# 带图形化界面的计算器
这是一个使用python编写带图形界面的简单计算器，可以用来练手。
### 项目架构

#### 1. 项目目录结构
```
calculator_project/
│
├── main.py
├── calculator/
│   ├── __init__.py
│   ├── gui.py
│   ├── operations.py
│   └── utils.py
└── README.md
```

#### 2. 各文件功能

- **main.py**: 项目的入口，启动图形化计算器。
- **calculator/__init__.py**: 标识 `calculator` 目录为一个 Python 包。
- **calculator/gui.py**: 包含创建和管理图形界面的代码。
- **calculator/operations.py**: 包含基本的数学运算函数。
- **calculator/utils.py**: 包含辅助函数和工具函数。
- **README.md**: 项目说明文件，描述项目的功能和使用方法。

### 具体代码实现

#### 1. **main.py**

```python
from calculator.gui import CalculatorGUI

if __name__ == "__main__":
    app = CalculatorGUI()
    app.run()
```

#### 2. **calculator/__init__.py**

```python
# 这个文件可以留空，或包含一些包级别的初始化代码。
```

#### 3. **calculator/gui.py**

```python
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
```

#### 4. **calculator/operations.py**

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
```

#### 5. **calculator/utils.py**

```python
# 可添加一些辅助函数，如输入验证、格式化等
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
```




