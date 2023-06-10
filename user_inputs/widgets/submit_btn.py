import ttkbootstrap as ttk
import time
import datetime
import sys
import threading

from booking.index import initialize_booking


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

        hotel_id, date = self.hotel_details.get_values()

        values["hotel_id"] = hotel_id
        values["date"] = date

        return values

    def start_program(self):
        t = threading.Thread(target=self.submit_form)
        t.start()
        print("hi")

    def submit_form(self):
        # Wait until schedulde time
        # target_time = datetime.time(1, 0)
        # current_datetime = datetime.datetime.now()
        # target_datetime = datetime.datetime.combine(
        #     current_datetime.date(), target_time
        # )

        # if current_datetime >= target_datetime:
        #     target_datetime += datetime.timedelta(days=1)

        # remaining_time = target_datetime - current_datetime
        # minutes_remaining = int(remaining_time.total_seconds() // 60)
        # hours = minutes_remaining // 60
        # minutes = minutes_remaining % 60
        # print(f"Sleeping for {hours} hours and {minutes} minutes")

        # time.sleep(remaining_time.total_seconds())

        # Retrieve user inputs
        form_values = self.get_forms_value()

        time.sleep(1)
        self.pack_time_label("12 minutes")

        # Start booking process
        initialize_booking(form_values)

        # self.root.destroy()
