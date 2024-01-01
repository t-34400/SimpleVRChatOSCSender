import tkinter as tk

class ChatboxParams:
    def __init__(self):
        self.chat_text_var = tk.StringVar()
        self.immediate_send_var = tk.BooleanVar()
        self.immediate_send_var.set(False)
        self.notify_sound_var = tk.BooleanVar()
        self.notify_sound_var.set(False)

        self.show_typing_indicator_var = tk.BooleanVar()
        self.show_typing_indicator_var.set(False)