import ttkbootstrap as ttk
from user_inputs.widgets.hotel_id import HotelIdWidget
from user_inputs.widgets.date import DateWidget


class HotelDetailsWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding="10")

        # Hotel ID
        self.hotel_id_widget = HotelIdWidget(self)
        self.hotel_id_widget.pack(anchor="w", pady=5)

        # Room row
        self.date_widget = DateWidget(self)
        self.date_widget.pack(anchor="w", pady=5)

    def get_values(self):
        hotel_id = self.hotel_id_widget.hotel_id_entry.get()
        date = self.date_widget.date_entry.get()

        return hotel_id, date
