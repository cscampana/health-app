import tkinter as tk
from tkinter import ttk
import main


def button_calculate(frame_bmi, height, weight, font_style_body):
    result = main.calculate_bmi_metric(weight=weight, height=height)
    text_result = ttk.Label(frame_bmi, text="Your BMI is: ", font=font_style_body)
    text_calculated = ttk.Label(frame_bmi, text="{:.{precision}f}".format(result, precision=2),
                                font=font_style_body)
    text_result.grid(row=4, column=0)
    text_calculated.grid(row=4, column=1)


class HealthMainView(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Health App")
        self.geometry("470x300")
        self.config(menu=self.menu())
        self.main_interface().pack()

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
        tab.add(self.bmi_tab(), text="BMI")

        return tab

    def bmi_tab(self):
        font_style_title = ("Arial", 20)
        font_style_body = ("Arial", 14)

        frame_bmi = ttk.Frame(width=self.winfo_width() - 10, height=self.winfo_height() - 10)

        # Row 0
        text_bmi = ttk.Label(frame_bmi, text="Body Mass Index calculator", font=font_style_title)
        text_bmi.grid(row=0, column=0, columnspan=2, sticky=tk.N)

        # Row 1
        text_input_weight = ttk.Label(frame_bmi, text="Input your weight: ", font=font_style_body)
        input_weight = ttk.Entry(frame_bmi, font=font_style_body)
        text_input_weight.grid(row=1, column=0, ipady=20, padx=20)
        input_weight.grid(row=1, column=1, padx=20)

        # Row 2
        text_input_height = ttk.Label(frame_bmi, text="Input your height: ", font=font_style_body)
        input_height = ttk.Entry(frame_bmi, font=font_style_body)
        text_input_height.grid(row=2, column=0, padx=20)
        input_height.grid(row=2, column=1, padx=20)
        # Row 3
        button_submit_bmi = ttk.Button(frame_bmi, text="Calculate",
                                       command=lambda: button_calculate(frame_bmi, input_height.get(),
                                                                        input_weight.get(), font_style_body))
        button_submit_bmi.grid(row=3, column=0, columnspan=2, ipady=12, pady=25, ipadx=60)

        return frame_bmi


if __name__ == '__main__':
    application = HealthMainView()
    application.mainloop()
