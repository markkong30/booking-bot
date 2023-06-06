from user_inputs.room_form import FormComponent


def add_form(root, content_frame, forms):
    # Create a new form component
    new_form = FormComponent(content_frame, index=len(forms))
    new_form.pack()

    # Append the new form to the list
    forms.append(new_form)

    # Update the geometry to accommodate the new forms
    root.update_idletasks()
    root.geometry(f"400x{len(forms) * 280}")
