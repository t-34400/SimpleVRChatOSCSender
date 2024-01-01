import tkinter as tk

class OSCReceiverConfig:
    config_change_callbacks = []

    def __init__(self):
        self.local_ip_var = tk.StringVar()
        self.local_ip_var.set("127.0.0.1")
        self.local_port_var = tk.IntVar()
        self.local_port_var.set(9000)
    
    def get_local_ip_and_port(self):
        return self.local_ip_var.get(), self.local_port_var.get()

    def register_config_change_callback(self, callback):
        self.config_change_callbacks.append(callback)

    def change_config(self):
        print(f"{len(self.config_change_callbacks)=}")
        for callback in self.config_change_callbacks:
            callback()
