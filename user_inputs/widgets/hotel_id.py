import ttkbootstrap as ttk


class HotelIdWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.hotel_id = ttk.Label(self, text="Hotel ID:")
        self.hotel_id.pack(side="left")

        self.hotel_id_entry = ttk.Entry(self)
        self.hotel_id_entry.pack(side="right", padx=5)
