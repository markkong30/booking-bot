import ttkbootstrap as ttk


class AddRoomButton(ttk.Button):
    def __init__(self, master, command):
        super().__init__(master, text="Add Room", command=command)
        self.command = command

    def add_room(self):
        print("add")
