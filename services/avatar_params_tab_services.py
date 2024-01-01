from models.avatar_param_sender_params import AvatarParamSenderParams

class AvatarParamsTabServices:
    def __init__(self, sender, params: AvatarParamSenderParams):
        self.sender = sender
        self.params = params

    def send_avatar_params(self):
        address = self.params.address_var.get()
        type = self.params.selected_type_var.get()
        value_string = self.params.value_var.get()

        value = AvatarParamsTabServices.try_parse(type, value_string)
        if value is not None:
            self.sender.send(address, [value])

    def send_new_avatar_params(self, address, value):
        self.sender.send(address, [value])

    def try_parse(type, value_string):
        try:
            if type == "Int":
                return int(value_string)
            elif type == "Float":
                return float(value_string)
            elif type == "Bool":
                if value_string == "False" or value_string == "false":
                    return False
                return bool(value_string) # return false if value_string is empty
            else:
                print(f"Failed to parse value string. Unknown value type: {type}")
                return None
        except:
            print("Failed to parse value string. Invalid value string")
            return None