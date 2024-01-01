from models.tracker_params import TrackerParams

class TrackerTabServices:
    position_address_format = "/tracking/trackers/{}/position"
    rotation_address_format = "/tracking/trackers/{}/rotation"

    def __init__(self, sender, params: TrackerParams):
        self.sender = sender
        self.params = params
        self.head_index = len(params.trackers) - 1

        for index, tracker_var in enumerate(self.params.tracker_vars):
            tracker_var.register_position_update_listener(lambda *_, index=index, tracker_var=tracker_var: self.on_position_update(index, tracker_var.get_position()))
            tracker_var.register_rotation_update_listener(lambda *_, index=index, tracker_var=tracker_var: self.on_rotation_update(index, tracker_var.get_euler_angles()))

    def on_position_update(self, index, position):
        if index == self.head_index:
            address = str.format(self.position_address_format, "head")
        else:
            address = str.format(self.position_address_format, index)

        self.sender.send(address, position)
        
    def on_rotation_update(self, index, euler_angles):
        if index == self.head_index:
            address = str.format(self.rotation_address_format, "head")
        else:
            address = str.format(self.rotation_address_format, index)

        self.sender.send(address, euler_angles)
        


