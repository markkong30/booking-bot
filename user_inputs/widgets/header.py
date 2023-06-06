import ttkbootstrap as ttk


class HeaderWidget(ttk.Frame):
    def __init__(self, master, index):
        super().__init__(master)
        self.index = index

        self.header = ttk.Label(
            self, text=f"Room {index + 1}", font=("Helvetica", 18, "bold")
        )
        self.header.pack(side="left")
