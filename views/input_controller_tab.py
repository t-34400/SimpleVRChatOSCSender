import tkinter as tk
from tkinter import ttk
from models.input_controller_params import InputControllerParams
from services.input_controller_tab_services import InputControllerTabServices

class InputControllerTab:
    def __init__(self, root, sender):
        self.input_controller_params = InputControllerParams()
        self.services = InputControllerTabServices(sender, self.input_controller_params)

        self.axes_group = ttk.LabelFrame(root, text="Axes")
        self.axes_group.pack(padx=10, pady=10, fill="both", expand=True, anchor=tk.W)

        for index, axis in enumerate(self.input_controller_params.axes):
            label = tk.Label(self.axes_group, text=axis, anchor=tk.W)
            label.grid(row=index, column=0, sticky="e", padx=5, pady=5)
            
            variable = self.input_controller_params.axis_vars[axis]

            scale = tk.Scale(self.axes_group, from_=-1.0, to=1.0, variable=variable, orient="horizontal", length=200, resolution=0.1)
            scale.grid(row=index, column=1, sticky="e", padx=5, pady=0)

            scale = tk.Entry(self.axes_group, textvariable=variable)
            scale.grid(row=index, column=2, sticky="e", padx=5, pady=0)

        self.buttons_group = ttk.LabelFrame(root, text="Buttons")
        self.buttons_group.pack(padx=10, pady=10, fill="both", expand=True, anchor=tk.W)

        for index, button in enumerate(self.input_controller_params.buttons):
            row = index // 3
            column = (index % 3) * 2

            label = tk.Label(self.buttons_group, text=button, anchor=tk.W)
            label.grid(row=row, column=column, sticky="e", padx=5, pady=5)

            variable = self.input_controller_params.button_vars[button]

            scale = tk.Checkbutton(self.buttons_group, variable=variable)
            scale.grid(row=row, column=column+1, sticky="e", padx=5, pady=0)