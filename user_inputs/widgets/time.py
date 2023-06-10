import ttkbootstrap as ttk
from tkinter import StringVar


class TimeLabel(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.time_label_text = StringVar()
        self.time_label = ttk.Label(self, textvariable=self.time_label_text)
        self.time_label.pack()

    def set_time(self, time):
        self.time_label_text.set(time)
