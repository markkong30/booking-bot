import tkinter as tk
import ttkbootstrap as ttk

root = ttk.Window(themename="journal")
root.title("Booking")
root.geometry("400x300")

# Create a frame to hold the content
content_frame = ttk.Frame(root, padding="20")
content_frame.pack(fill="both", expand=True)
content_frame.place(relx=0.5, rely=0.5, anchor="center")


# Date input
date_frame = ttk.Frame(content_frame)
date_frame.pack(anchor="w", pady=5)

date_label = ttk.Label(date_frame, text="Date:")
date_label.pack(side="left")

date_entry = ttk.Entry(date_frame)
date_entry.pack(side="right", padx=5)


# Number of people
people_frame = ttk.Frame(content_frame)
people_frame.pack(anchor="w", pady=5)

people_label = ttk.Label(people_frame, text="Number of People:")
people_label.pack(side="left")

people_dropdown = ttk.Combobox(people_frame, values=[1, 2, 3, 4], state="readonly")
people_dropdown.pack(side="right", padx=5)


# Room Type
room_frame = ttk.Frame(content_frame)
room_frame.pack(anchor="w", pady=5)

room_label = ttk.Label(room_frame, text="Room Type:")
room_label.pack(side="left")

room_var = tk.StringVar()
single_radio = ttk.Radiobutton(
    room_frame, text="Single", value="single", variable=room_var
)
single_radio.pack(side="right", padx=5)

double_radio = ttk.Radiobutton(
    room_frame, text="Double", value="double", variable=room_var
)
double_radio.pack(side="right", padx=5)

twin_radio = ttk.Radiobutton(room_frame, text="Twin", value="twin", variable=room_var)
twin_radio.pack(side="right", padx=5)


# Hotel ID
hotel_frame = ttk.Frame(content_frame)
hotel_frame.pack(anchor="w", pady=5)

hotel_label = ttk.Label(hotel_frame, text="Hotel ID:")
hotel_label.pack(side="left")

hotel_entry = ttk.Entry(hotel_frame)
hotel_entry.pack(side="right", padx=5)


# Row Number
row_frame = ttk.Frame(content_frame)
row_frame.pack(anchor="w", pady=5)

row_label = ttk.Label(row_frame, text="Row Number:")
row_label.pack(side="left")

row_entry = ttk.Entry(row_frame)
row_entry.pack(side="right", padx=5)


# Submit button
submit_button = ttk.Button(content_frame, text="Submit")
submit_button.pack(pady=15, anchor="center")


root.mainloop()
