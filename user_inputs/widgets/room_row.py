import ttkbootstrap as ttk


class RoomRowWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.room_row = ttk.Label(self, text="Room Row:")
        self.room_row.pack(side="left")

        self.room_row_entry = ttk.Entry(self)
        self.room_row_entry.pack(side="right", padx=5)
