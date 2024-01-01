import tkinter as tk
import threading

class ReceivedAvatarParam:
    def __init__(self, value):
        if isinstance(value, bool):
            self.value_var = tk.BooleanVar()
            self.sender_value_var = tk.BooleanVar()
        elif isinstance(value, int):
            self.value_var = tk.IntVar()
            self.sender_value_var = tk.IntVar()
        elif isinstance(value, float):
            self.value_var = tk.DoubleVar()
            self.sender_value_var = tk.DoubleVar()
        else:
            print(f"It's of an unknown type: {value}")
            self.value_var = tk.BooleanVar()
            self.sender_value_var = tk.BooleanVar()

        self.value_var.set(value)
        self.sender_value_var.set(value)

    def get_sender_value(self):
        return self.sender_value_var.get()
    
    def get_variables(self):
        return self.value_var, self.sender_value_var

    def set_new_value(self, value):
        self.value_var.set(value)


class ReceivedAvatarParams:
    received_params_lock = threading.Lock()
    received_params = {}
    on_update_callbacks = []

    def register_update_callback(self, callback):
        self.on_update_callbacks.append(callback)

    def add_received_param(self, address, value):
        self.received_params_lock.acquire()

        if address in self.received_params:
            self.received_params[address].set_new_value(value)
        else:
            param = ReceivedAvatarParam(value)
            self.received_params[address] = param

            for callback in self.on_update_callbacks:
                callback()

        self.received_params_lock.release()

