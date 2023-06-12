import time
import datetime

import ttkbootstrap as ttk
from tkinter import StringVar


class TimeLabel(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.time_label_text = StringVar()
        self.time_label = ttk.Label(self, textvariable=self.time_label_text)
        self.time_label.pack()

    def set_time(self, remaining_time):
        minutes_remaining = int(remaining_time.total_seconds() // 60)

        while minutes_remaining > 0:
            hours = minutes_remaining // 60
            minutes = minutes_remaining % 60
            time_label = f"{hours} hours and {minutes} minutes"
            print(time_label)
            self.time_label_text.set(f"Booking will start in {time_label}...")

            # Wait for 1 minute before updating the label again
            time.sleep(60)

            # Update the remaining time
            remaining_time -= datetime.timedelta(minutes=1)
            minutes_remaining = int(remaining_time.total_seconds() // 60)

        # Booking starts
        self.time_label_text.set("Booking has started!")
