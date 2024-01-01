from tkinter import ttk
from .avatar_params_tab import AvatarParamsTab
from .input_controller_tab import InputControllerTab
from .chatbox_tab import ChatboxTab
from .tracker_tab import TrackerTab
from .osc_config_tab import OSCConfigTab

class App:
    def __init__(self, root, sender, sender_config, receiver_config, received_avatar_params):
        self.root = root
        self.root.title("VRChat OSC Sender")

        self.notebook = ttk.Notebook(root)

        self.avatar_params_frame = ttk.Frame(self.notebook)
        AvatarParamsTab(self.avatar_params_frame, sender, received_avatar_params)
        self.notebook.add(self.avatar_params_frame, text="Avatar params")

        self.input_controller_frame = ttk.Frame(self.notebook)
        InputControllerTab(self.input_controller_frame, sender)
        self.notebook.add(self.input_controller_frame, text="Input Controller")

        self.chatbox_tab_frame = ttk.Frame(self.notebook)
        ChatboxTab(self.chatbox_tab_frame, sender)
        self.notebook.add(self.chatbox_tab_frame, text="Chatbox")

        self.tracker_tab_frame = ttk.Frame(self.notebook)
        TrackerTab(self.tracker_tab_frame, sender)
        self.notebook.add(self.tracker_tab_frame, text="Trackers")

        self.osc_config_frame = ttk.Frame(self.notebook)
        OSCConfigTab(self.osc_config_frame, sender_config, receiver_config)
        self.notebook.add(self.osc_config_frame, text="OSC config")

        self.notebook.pack(padx=10, pady=10)
