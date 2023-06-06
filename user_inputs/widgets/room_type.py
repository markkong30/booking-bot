import ttkbootstrap as ttk
import tkinter as tk


class RoomWidget(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.room_label = ttk.Label(self, text="Room Type:")
        self.room_label.pack(side="left")

        self.room_var = tk.StringVar()
        self.single_radio = ttk.Radiobutton(
            self, text="Single", value="single", variable=self.room_var
        )
        self.single_radio.pack(side="left", padx=5)

        self.double_radio = ttk.Radiobutton(
            self, text="Double", value="double", variable=self.room_var
        )
        self.double_radio.pack(side="left", padx=5)

        self.twin_radio = ttk.Radiobutton(
            self, text="Twin", value="twin", variable=self.room_var
        )
        self.twin_radio.pack(side="left", padx=5)
