import ttkbootstrap as ttk
import tkinter as tk


class StartNowWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.start_now_label = ttk.Label(self, text="Start Now? :")
        self.start_now_label.pack(side="left")

        self.start_now_var = tk.StringVar(value="no")  # Set the initial value to "no"

        self.yes_radio = ttk.Radiobutton(
            self, text="Yes", value="yes", variable=self.start_now_var
        )
        self.yes_radio.pack(side="left", padx=5)

        self.no_radio = ttk.Radiobutton(
            self, text="No", value="no", variable=self.start_now_var
        )
        self.no_radio.pack(side="left", padx=5)
