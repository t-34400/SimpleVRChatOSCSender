import tkinter as tk
from tkinter import ttk
from models.chatbox_params import ChatboxParams
from services.chatbox_tab_services import ChatboxTabServices

class ChatboxTab:
    def __init__(self, root, sender):
        self.params = ChatboxParams()
        self.services = ChatboxTabServices(sender, self.params)

        self.chat_text_group = ttk.LabelFrame(root, text="Chat")
        self.chat_text_group.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X, expand=False)

        self.text_input_frame = tk.Frame(self.chat_text_group)
        self.text_input_frame.pack()

        self.text_input_label = tk.Label(self.text_input_frame, text="Text: ")
        self.text_input_label.pack(side=tk.LEFT)

        self.text_input = tk.Entry(self.text_input_frame, textvariable=self.params.chat_text_var, width=52)
        self.text_input.bind("<Return>", self.press_enter_key)
        self.text_input.pack(side=tk.LEFT, ipadx=5)

        self.send_button = tk.Button(self.text_input_frame, text="Send", command=self.services.send_chat_text)
        self.send_button.pack(side=tk.LEFT, ipadx=5)

        self.options_frame = tk.Frame(self.chat_text_group)
        self.options_frame.pack()

        self.immediate_send_label = tk.Label(self.options_frame, text="Immediate send: ")
        self.immediate_send_label.grid(row=0, column=0)

        self.immediate_send_checkbutton = tk.Checkbutton(self.options_frame, variable=self.params.immediate_send_var)
        self.immediate_send_checkbutton.grid(row=0, column=1)

        self.notify_sound_label = tk.Label(self.options_frame, text="Notify sound: ")
        self.notify_sound_label.grid(row=1, column=0)

        self.notify_sound_checkbutton = tk.Checkbutton(self.options_frame, variable=self.params.notify_sound_var)
        self.notify_sound_checkbutton.grid(row=1, column=1)

        self.toggle_indicator_group = tk.Frame(root)
        self.toggle_indicator_group.pack(side=tk.TOP, padx=10, pady=10)

        self.toggle_indicator_label = tk.Label(self.toggle_indicator_group, text="Show typing Indicator: ")
        self.toggle_indicator_label.pack(side=tk.LEFT)

        self.toggle_indicator_checkbutton = tk.Checkbutton(self.toggle_indicator_group, variable=self.params.show_typing_indicator_var)
        self.toggle_indicator_checkbutton.pack(side=tk.LEFT, ipadx=5)

    def press_enter_key(self, _):
        self.services.send_chat_text()

