import tkinter as tk
from tkinter import ttk


class HealthMainView(tk.Tk):

    def ___init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title("Health App")
        self.geometry("800x600")


if __name__ == '__main__':
    application = HealthMainView()
    application.mainloop()

