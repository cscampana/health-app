import tkinter as tk
from tkinter import ttk


class HealthMainView(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Health App")
        self.geometry("800x600")
        self.config(menu=self.menu())
        self.main_interface().grid(row=0,column=0, sticky=tk.N)

    def menu(self):
        main_menu = tk.Menu(self)
        file_menu = tk.Menu(main_menu, tearoff=False)
        file_menu.add('command', label='Open')
        file_menu.add('command', label='Save')
        file_menu.add('command', label='Save As')
        file_menu.add('command', label='Exit', command=self.quit())
        main_menu.add_cascade(label='File', menu=file_menu)
        main_menu.add('command', label='About', command=self)
        return main_menu

    def main_interface(self):
        tab = ttk.Notebook(self)
        frame_bmi = ttk.Frame(tab,width=self.winfo_width()-10, height=self.winfo_height()-10)
        text_bmi = ttk.Label(frame_bmi, text="Body Mass Index calculator")
        text_bmi.grid(row=0, column=0, sticky=tk.N)
        tab.add(frame_bmi, text="BMI")
        return tab


if __name__ == '__main__':
    application = HealthMainView()
    application.mainloop()

