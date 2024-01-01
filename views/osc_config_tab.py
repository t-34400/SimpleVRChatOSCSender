import tkinter as tk
from services.osc_config_tab_service import OSCConfigTabService

class OSCConfigTab:
    def __init__(self, root, sender_config, receiver_config):
        self.root = root
        self.service = OSCConfigTabService(receiver_config)

        self.remote_ip_var = sender_config.remote_ip_var
        self.remote_port_var = sender_config.remote_port_var
        self.local_ip_var = receiver_config.local_ip_var
        self.local_port_var = receiver_config.local_port_var

        self.sender_group = tk.LabelFrame(root, text="Sender")
        self.sender_group.pack(padx=10, pady=10, ipady=10, fill=tk.X, side=tk.TOP)

        self.remote_ip_label = tk.Label(self.sender_group, text="Remote IP address:", anchor=tk.W)
        self.remote_ip_label.pack(pady=5)

        self.remote_ip_entry = tk.Entry(self.sender_group, textvariable=self.remote_ip_var, width=40)
        self.remote_ip_entry.pack()

        self.remote_port_label = tk.Label(self.sender_group, text="Remote port:", anchor=tk.W)
        self.remote_port_label.pack(pady=5)

        self.remote_port_entry = tk.Entry(self.sender_group, textvariable=self.remote_port_var, width=40)
        self.remote_port_entry.pack()

        self.receiver_group = tk.LabelFrame(root, text="Receiver")
        self.receiver_group.pack(padx=10, pady=10, ipady=10, fill=tk.X, side=tk.TOP)

        self.local_ip_label = tk.Label(self.receiver_group, text="Local IP address:", anchor=tk.W)
        self.local_ip_label.pack(pady=5)

        self.local_ip_entry = tk.Entry(self.receiver_group, textvariable=self.local_ip_var, width=40)
        self.local_ip_entry.pack()

        self.local_port_label = tk.Label(self.receiver_group, text="Local port:", anchor=tk.W)
        self.local_port_label.pack(pady=5)

        self.local_port_entry = tk.Entry(self.receiver_group, textvariable=self.local_port_var, width=40)
        self.local_port_entry.pack()

        self.local_config_set_button = tk.Button(self.receiver_group, text="Rebuild Receiver Server", command=self.service.change_config)
        self.local_config_set_button.pack()