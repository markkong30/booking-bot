import ttkbootstrap as ttk


class SubmitButton(ttk.Button):
    def __init__(self, master, forms):
        super().__init__(
            master, text="Submit", command=self.get_forms_value, bootstyle="info"
        )
        self.forms = forms

    def get_forms_value(self):
        values = {}
        for i, form in enumerate(self.forms):
            date, number_of_people, room_type = form.get_values()
            values[f"room_{i}"] = {
                "date": date,
                "number_of_people": number_of_people,
                "room_type": room_type,
            }
        print(values)
        return values
