import ttkbootstrap as ttk


class PeopleWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.people_label = ttk.Label(self, text="Number of People:")
        self.people_label.pack(side="left")

        self.people_dropdown = ttk.Combobox(self, values=[1, 2, 3, 4], state="readonly")
        self.people_dropdown.pack(side="right", padx=5)
