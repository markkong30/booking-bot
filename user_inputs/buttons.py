import ttkbootstrap as ttk
from user_inputs.widgets.add_room_btn import AddRoomButton
from user_inputs.widgets.submit_btn import SubmitButton


class ButtonsWidget(ttk.Frame):
    def __init__(self, master, add_form, root, forms, hotel_details, pack_time_label):
        super().__init__(master)
        self.add_form = add_form
        self.root = root
        self.forms = forms
        self.hotel_details = hotel_details
        self.pack_time_label = pack_time_label

        # Create a frame to hold the buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(side="bottom", pady=30)

        # Add room button
        self.add_room_btn = AddRoomButton(
            button_frame, lambda: self.add_form(self.root, self, self.forms)
        )
        self.add_room_btn.pack(side="left", padx=35)

        # Submit button
        self.submit_btn = SubmitButton(
            button_frame,
            self.forms,
            self.hotel_details,
            self.root,
            self.pack_time_label,
            self,
        )
        self.submit_btn.pack(side="right", padx=35)
