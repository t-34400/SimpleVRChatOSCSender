import tkinter as tk

class AvatarParamSenderParams:
    types = [ "Int", "Bool", "Float" ]

    def __init__(self):
        self.address_var = tk.StringVar()
        self.address_var.set("/avatar/parameters/VelocityZ")
        self.selected_type_var = tk.StringVar()
        self.selected_type_var.set(self.types[2])
        self.value_var = tk.StringVar()
        self.value_var.set("0")
