import ttkbootstrap as ttk

from user_inputs.room_form import FormComponent
from user_inputs.widgets.submit_btn import SubmitButton
from user_inputs.widgets.add_room_btn import AddRoomButton
from user_inputs.utils import add_form


root = ttk.Window(themename="journal")
root.title("Booking")
root.geometry("400x300")

# Create a frame to hold the content
content_frame = ttk.Frame(root, padding="20")
content_frame.pack(fill="both", expand=True)
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a list to keep track of the forms
forms = []


# Create the initial form component
initial_form = FormComponent(content_frame, index=0)
initial_form.pack()
forms.append(initial_form)


# Create a frame to hold the buttons
button_frame = ttk.Frame(content_frame)
button_frame.pack(side="bottom", pady=30)

# Add room button
add_room_btn = AddRoomButton(button_frame, lambda: add_form(root, content_frame, forms))
add_room_btn.pack(side="left", padx=35)

# Submit button
submit_btn = SubmitButton(button_frame, forms)
submit_btn.pack(side="right", padx=35)

root.mainloop()
