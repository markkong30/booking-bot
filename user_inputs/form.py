import ttkbootstrap as ttk

from user_inputs.widgets.date import DateWidget
from user_inputs.widgets.people import PeopleWidget
from user_inputs.widgets.room_type import RoomWidget
from user_inputs.widgets.submit_btn import SubmitButton


class FormComponent(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding="20")

        # Date input
        self.date_widget = DateWidget(self)
        self.date_widget.pack(anchor="w", pady=5)

        # Number of people
        self.people_widget = PeopleWidget(self)
        self.people_widget.pack(anchor="w", pady=5)

        # Room type
        self.room_widget = RoomWidget(self)
        self.room_widget.pack(anchor="w", pady=5)

        # Submit button
        submit_button = SubmitButton(self, self)
        submit_button.pack(pady=10)

    def get_form_values(self):
        date_value = self.date_widget.date_entry.get()
        people_value = self.people_widget.people_dropdown.get()
        room_value = self.room_widget.room_var.get()

        return date_value, people_value, room_value
