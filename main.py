import ttkbootstrap as ttk

from user_inputs.hotel_details import HotelDetailsWidget
from user_inputs.room_form import FormComponent
from user_inputs.buttons import ButtonsWidget
from user_inputs.utils import add_form


root = ttk.Window(themename="journal")
root.title("Booking")
root.geometry("400x400")

# Create a frame to hold the content
content_frame = ttk.Frame(root, padding="20")
content_frame.pack(fill="both", expand=True)
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Create a list to keep track of the forms
forms = []


hotel_details = HotelDetailsWidget(content_frame)
hotel_details.pack()

# Create the initial form component
initial_form = FormComponent(content_frame, index=0)
initial_form.pack()
forms.append(initial_form)

cta_btns = ButtonsWidget(
    content_frame,
    root=root,
    forms=forms,
    add_form=add_form,
    hotel_details=hotel_details,
)
cta_btns.pack()


root.mainloop()
