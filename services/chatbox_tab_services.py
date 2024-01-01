from models.chatbox_params import ChatboxParams

class ChatboxTabServices:
    chatbox_address = "/chatbox/input"
    toggle_indicator_address = "/chatbox/typing"

    def __init__(self, sender, params: ChatboxParams):
        self.sender = sender
        self.params = params

        self.params.show_typing_indicator_var.trace_add("write", lambda *_: self.toggle_typing_indicator())

    def send_chat_text(self):
        address = self.chatbox_address
        text_input = self.params.chat_text_var.get()
        if text_input == "":
            return
        self.params.chat_text_var.set("")
        immediate_send = self.params.immediate_send_var.get()
        notify_sound = self.params.notify_sound_var.get()

        self.sender.send(address, [text_input, immediate_send, notify_sound])

    def toggle_typing_indicator(self):
        address = self.toggle_indicator_address
        is_on = self.params.show_typing_indicator_var.get()

        self.sender.send(address, [is_on])