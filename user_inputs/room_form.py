import ttkbootstrap as ttk

from user_inputs.widgets.date import DateWidget
from user_inputs.widgets.people import PeopleWidget
from user_inputs.widgets.room_type import RoomWidget
from user_inputs.widgets.header import HeaderWidget
from user_inputs.widgets.add_room_btn import AddRoomButton


class FormComponent(ttk.Frame):
    def __init__(self, master, index=None):
        super().__init__(master, padding="10")
        self.index = index

        # Create a frame for the header and add_room_btn
        header_frame = ttk.Frame(self)
        header_frame.pack(anchor="w", pady=5)

        # Room header
        self.room_header = HeaderWidget(header_frame, self.index)
        self.room_header.pack(side="left")

        # Date input
        self.date_widget = DateWidget(self)
        self.date_widget.pack(anchor="w", pady=5)

        # Number of people
        self.people_widget = PeopleWidget(self)
        self.people_widget.pack(anchor="w", pady=5)

        # Room type
        self.room_widget = RoomWidget(self)
        self.room_widget.pack(anchor="w", pady=5)

    def get_values(self):
        date = self.date_widget.date_entry.get()
        number_of_people = self.people_widget.people_dropdown.get()
        room_type = self.room_widget.room_var.get()

        return date, number_of_people, room_type
