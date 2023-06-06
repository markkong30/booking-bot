import ttkbootstrap as ttk


class SubmitButton(ttk.Button):
    def __init__(self, master, form):
        super().__init__(master, text="Submit", command=self.submit_form)
        self.form = form
        self.pack(pady=10)

    def submit_form(self):
        form_values = self.form.get_form_values()
        # Process the form values
        print("Form Values:", form_values)
