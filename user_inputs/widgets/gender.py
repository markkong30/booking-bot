import ttkbootstrap as ttk
import tkinter as tk


class GenderWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.gender_label = ttk.Label(self, text="Gender:")
        self.gender_label.pack(side="left")

        self.gender_var = tk.StringVar()
        self.male_radio = ttk.Radiobutton(
            self, text="Male", value="male", variable=self.gender_var
        )
        self.male_radio.pack(side="left", padx=5)

        self.female_radio = ttk.Radiobutton(
            self, text="Female", value="female", variable=self.gender_var
        )
        self.female_radio.pack(side="left", padx=5)
