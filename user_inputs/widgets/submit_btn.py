import ttkbootstrap as ttk
import time
import datetime
import threading

from booking.index import initialize_booking
from booking.constants import booking_time
from booking.utils import has_empty_strings


class SubmitButton(ttk.Button):
    def __init__(
        self, master, forms, hotel_details, root, pack_time_label, content_frame
    ):
        super().__init__(
            master, text="Submit", command=self.start_program, bootstyle="info"
        )
        self.forms = forms
        self.hotel_details = hotel_details
        self.root = root
        self.pack_time_label = pack_time_label
        self.content_frame = content_frame

    def get_forms_value(self):
        values = {}
        for i, form in enumerate(self.forms):
            (
                number_of_people,
                room_type,
                first_name,
                last_name,
                gender,
            ) = form.get_values()
            values[f"room_{i + 1}"] = {
                "number_of_people": number_of_people,
                "room_type": room_type,
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
            }

        hotel_id, date, start_now = self.hotel_details.get_values()

        values["hotel_id"] = hotel_id
        values["date"] = date
        values["start_now"] = start_now

        return values

    def start_program(self):
        t = threading.Thread(target=self.submit_form)
        t.start()

    def submit_form(self):
        # Retrieve user inputs
        form_values = self.get_forms_value()

        if has_empty_strings(form_values):
            print(form_values)
            return print("Empty")

        # Start booking process immediately if start now is checked
        if form_values["start_now"] == "yes":
            self.pack_time_label(datetime.timedelta(seconds=0))
            return initialize_booking(form_values)

        # Wait until schedulde time
        target_time = datetime.time(int(booking_time), 0)
        current_datetime = datetime.datetime.now()
        target_datetime = datetime.datetime.combine(
            current_datetime.date(), target_time
        )

        if current_datetime >= target_datetime:
            target_datetime += datetime.timedelta(days=1)

        remaining_time = target_datetime - current_datetime

        self.pack_time_label(remaining_time)
        time.sleep(remaining_time.total_seconds())

        # Start booking process
        initialize_booking(form_values)
