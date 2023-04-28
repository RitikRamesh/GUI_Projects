import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=20, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, command=lambda key=button: self.click(key)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        tk.Button(master, text='C', width=5, height=2, command=self.clear).grid(row=5, column=0, padx=5, pady=5)
        
    def click(self, key):
        if key == '=':

            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, 'Error')
        else:

            self.display.insert(tk.END, key)
    
    def clear(self):
        self.display.delete(0, tk.END)

root = tk.Tk()
root.geometry('365x315')
root.resizable(0,0)
calculator = Calculator(root)
root.mainloop()