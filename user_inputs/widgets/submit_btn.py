import ttkbootstrap as ttk

from booking.index import initialize_booking


class SubmitButton(ttk.Button):
    def __init__(self, master, forms, hotel_details, root):
        super().__init__(
            master, text="Submit", command=self.submit_form, bootstyle="info"
        )
        self.forms = forms
        self.hotel_details = hotel_details
        self.root = root

    def get_forms_value(self):
        values = {}
        for i, form in enumerate(self.forms):
            number_of_people, room_type = form.get_values()
            values[f"room_{i + 1}"] = {
                "number_of_people": number_of_people,
                "room_type": room_type,
            }

        hotel_id, date = self.hotel_details.get_values()

        values["hotel_id"] = hotel_id
        values["date"] = date

        return values

    def submit_form(self):
        form_values = self.get_forms_value()

        initialize_booking(form_values)
        self.root.destroy()
