import ttkbootstrap as ttk

from user_inputs.form import FormComponent
from booking.index import initialize_booking


root = ttk.Window(themename="journal")
root.title("Booking")
root.geometry("400x300")

# Create a frame to hold the content
content_frame = ttk.Frame(root, padding="20")
content_frame.pack(fill="both", expand=True)
content_frame.place(relx=0.5, rely=0.5, anchor="center")


# Create the form component
form = FormComponent(content_frame)
form.pack()


root.mainloop()
