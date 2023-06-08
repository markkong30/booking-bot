import ttkbootstrap as ttk


class FirstNameWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.first_name_label = ttk.Label(self, text="First Name:")
        self.first_name_label.pack(side="left")

        self.first_name_entry = ttk.Entry(self)
        self.first_name_entry.pack(side="right", padx=5)


class LastNameWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.last_name_label = ttk.Label(self, text="Last Name:")
        self.last_name_label.pack(side="left")

        self.last_name_entry = ttk.Entry(self)
        self.last_name_entry.pack(side="right", padx=5)
