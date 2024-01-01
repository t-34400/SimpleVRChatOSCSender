import tkinter as tk
from tkinter import ttk
from models.tracker_params import TrackerParams
from services.tracker_tab_services import TrackerTabServices

class TrackerTab:
    def __init__(self, root, sender):
        self.params = TrackerParams()
        self.services = TrackerTabServices(sender, self.params)

        self.sender_group = ttk.LabelFrame(root, text="Tracker Data")
        self.sender_group.pack(padx=10, pady=10, fill="both", expand=True)

        component_labels = [ "x", "y", "z" ]

        for index, tracker_var in enumerate(self.params.tracker_vars):
            row = index * 2

            label = self.params.trackers[index]
            tracker_label = tk.Label(self.sender_group, text=label)
            tracker_label.grid(row=row, column=0, rowspan=2)

            position_label = tk.Label(self.sender_group, text="position")
            position_label.grid(row=row, column=1)

            rotation_label = tk.Label(self.sender_group, text="rotation")
            rotation_label.grid(row=row+1, column=1)

            column = 2
            for index, label in enumerate(component_labels):
                position_component_var = tracker_var.position_components[index]
                rotation_component_var = tracker_var.rotation_components[index]

                position_component_label = tk.Label(self.sender_group, text=label)
                rotation_component_label = tk.Label(self.sender_group, text=label)
                position_component_label.grid(row=row, column=column, padx=5, pady=10)
                rotation_component_label.grid(row=row+1, column=column, padx=5)
                column += 1

                position_component_input = tk.Entry(self.sender_group, textvariable=position_component_var)
                rotation_component_input = tk.Entry(self.sender_group, textvariable=rotation_component_var)
                position_component_input.grid(row=row, column=column, padx=5)
                rotation_component_input.grid(row=row+1, column=column, padx=5)
                column += 1
            
