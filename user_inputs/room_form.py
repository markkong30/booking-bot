import ttkbootstrap as ttk

from user_inputs.widgets.people import PeopleWidget
from user_inputs.widgets.room_type import RoomWidget
from user_inputs.widgets.header import HeaderWidget
from user_inputs.widgets.name import FirstNameWidget, LastNameWidget
from user_inputs.widgets.gender import GenderWidget


class FormComponent(ttk.Frame):
    def __init__(self, master, index=None):
        super().__init__(master, padding="10")
        self.index = index
        self.first_name_widget = None
        self.last_name_widget = None
        self.gender_widget = None

        # Room header
        self.room_header = HeaderWidget(self, self.index)
        self.room_header.pack(anchor="w", pady=5)

        if index != 0:
            # First name
            self.first_name_widget = FirstNameWidget(self)
            self.first_name_widget.pack(anchor="w", pady=5)

            # Last name
            self.last_name_widget = LastNameWidget(self)
            self.last_name_widget.pack(anchor="w", pady=5)

            # Gender
            self.gender_widget = GenderWidget(self)
            self.gender_widget.pack(anchor="w", pady=5)

        # Number of people
        self.people_widget = PeopleWidget(self)
        self.people_widget.pack(anchor="w", pady=5)

        # Room type
        self.room_widget = RoomWidget(self)
        self.room_widget.pack(anchor="w", pady=5)

    def get_values(self):
        number_of_people = self.people_widget.people_dropdown.get()
        room_type = self.room_widget.room_var.get()

        first_name_entry = getattr(self.first_name_widget, "first_name_entry", None)
        first_name = first_name_entry.get() if first_name_entry else ""

        last_name_entry = getattr(self.last_name_widget, "last_name_entry", None)
        last_name = last_name_entry.get() if last_name_entry else ""

        gender_var = getattr(self.gender_widget, "gender_var", None)
        gender = gender_var.get() if gender_var else ""

        return number_of_people, room_type, first_name, last_name, gender
