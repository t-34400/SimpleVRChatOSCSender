class OSCConfigTabService:
    def __init__(self, receiver_config):
        self.receiver_config = receiver_config

    def change_config(self):
        self.receiver_config.change_config()