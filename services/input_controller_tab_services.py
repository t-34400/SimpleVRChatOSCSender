from models.input_controller_params import InputControllerParams

class InputControllerTabServices:
    axis_address_prefix = "/input/"
    button_address_prefix = "/input/"

    def __init__(self, sender, params: InputControllerParams):
        self.sender = sender
        self.params = params

        for axis in self.params.axes:
            variable = self.params.axis_vars[axis]
            variable.trace_add("write", lambda *args, axis=axis, variable=variable: self.send_axis_value(axis, variable))

        for button in self.params.buttons:
            variable = self.params.button_vars[button]
            variable.trace_add("write", lambda *args, button=button, variable=variable: self.send_button_value(button, variable))
    
    def send_axis_value(self, axis, variable):
        address = self.axis_address_prefix + axis
        value = variable.get()
        
        self.sender.send(address, [value])

    def send_button_value(self, button, variable):
        address = self.button_address_prefix + button
        if variable.get():
            value = 1
        else:
            value = 0

        self.sender.send(address, [value])
