import tkinter as tk
from tkinter import ttk
from models.received_avatar_params import ReceivedAvatarParams
from models.avatar_param_sender_params import AvatarParamSenderParams
from services.avatar_params_tab_services import AvatarParamsTabServices

class AvatarParamsTab:
    received_address_list = []

    def __init__(self, root, sender, received_params: ReceivedAvatarParams):
        self.root = root
        self.params = AvatarParamSenderParams()
        self.services = AvatarParamsTabServices(sender, self.params)
        self.received_params = received_params

        self.set_sender_components(root)
        self.received_params.register_update_callback(self.set_received_params_components)


    def set_sender_components(self, root):
        self.sender_group = ttk.LabelFrame(root, text="Avatar Parameter Sender")
        self.sender_group.pack(padx=10, pady=10, fill=tk.X)

        self.sender_param_frame = tk.Frame(self.sender_group)
        self.sender_param_frame.pack()

        self.address_label = tk.Label(self.sender_param_frame, text="Address:")
        self.address_label.grid(row=0, column=0)

        self.address_entry = tk.Entry(self.sender_param_frame, textvariable=self.params.address_var, width=40)
        self.address_entry.grid(row=0, column=1, columnspan=2)

        self.value_label = tk.Label(self.sender_param_frame, text="Value:")
        self.value_label.grid(row=1, column=0)

        self.dropdown = ttk.Combobox(self.sender_param_frame, values=self.params.types, textvariable=self.params.selected_type_var, width=10)
        self.dropdown.grid(row=1, column=1)

        self.value_entry = tk.Entry(self.sender_param_frame, textvariable=self.params.value_var)
        self.value_entry.grid(row=1, column=2)
        
        self.send_button = tk.Button(self.sender_group, text="Send avatar parameter", command=self.services.send_avatar_params)
        self.send_button.pack(side=tk.TOP, pady=10)

    def set_received_params_components(self):
        self.received_params_group = ttk.LabelFrame(self.root, text="Received Avatar Parameters")
        self.received_params_group.pack(padx=10, pady=10, fill=tk.X)

        for address, received_param in self.received_params.received_params.items():
            if address not in self.received_address_list:
                index = len(self.received_address_list)
                received_value_var, sender_value_var = received_param.get_variables()

                label = tk.Label(self.received_params_group, text=address+":")
                label.grid(row=index, column=0, padx=5, pady=5)

                received_value_label = tk.Label(self.received_params_group, textvariable=received_value_var)
                received_value_label.grid(row=index, column=1, padx=5)

                label = tk.Label(self.received_params_group, text="   ->   ")
                label.grid(row=index, column=2, padx=5)

                sender_value_input = tk.Entry(self.received_params_group, textvariable=sender_value_var)
                sender_value_input.grid(row=index, column=3, padx=5)

                send_button = tk.Button(self.received_params_group, text="Send", command=lambda *_, address=address, var=sender_value_var: self.services.send_new_avatar_params(address, var.get()))
                send_button.grid(row=index, column=4, padx=5)

