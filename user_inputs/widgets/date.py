import ttkbootstrap as ttk


class DateWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.date_label = ttk.Label(self, text="Date:")
        self.date_label.pack(side="left")

        self.date_entry = ttk.Entry(self)
        self.date_entry.pack(side="right", padx=5)
