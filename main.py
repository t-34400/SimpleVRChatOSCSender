import tkinter as tk
from models.osc_sender_config import OSCSenderConfig
from models.osc_receiver_config import OSCReceiverConfig
from models.received_avatar_params import ReceivedAvatarParams
from osc.osc_sender import OSCSender
from osc.osc_receiver import OSCReceiver
from views.app import App

if __name__ == "__main__":
    root = tk.Tk()

    sender_config = OSCSenderConfig()
    sender = OSCSender(sender_config)
    receiver_config = OSCReceiverConfig()
    received_avatar_params = ReceivedAvatarParams()
    receiver = OSCReceiver(receiver_config, received_avatar_params)

    app = App(root, sender, sender_config, receiver_config, received_avatar_params)
    root.mainloop()

    receiver.close()

