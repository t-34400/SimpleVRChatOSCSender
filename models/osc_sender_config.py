import tkinter as tk

class OSCSenderConfig:
    def __init__(self):
        self.remote_ip_var = tk.StringVar()
        self.remote_ip_var.set("127.0.0.1")
        self.remote_port_var = tk.IntVar()
        self.remote_port_var.set(9000)

    def get_remote_ip(self):
        return self.remote_ip_var.get()
    
    def get_remote_port(self):
        return self.remote_port_var.get()
    