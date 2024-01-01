from pythonosc import osc_message_builder
from pythonosc import udp_client

class OSCSender:
    current_remote_ip = "127.0.0.1"
    current_remote_port = 9000

    def __init__(self, config):
        self.config = config
        self.create_udp_client(self.current_remote_ip, self.current_remote_port)

    def create_udp_client(self, remote_ip, remote_port):
        self.current_remote_ip = remote_ip
        self.current_remote_port = remote_port
        self.client = udp_client.SimpleUDPClient(remote_ip, remote_port)
        print(f"Created OSC sender client for {remote_ip}:{remote_port}")

    def send(self, osc_address, osc_arguments):
        remote_ip = self.config.get_remote_ip()
        remote_port = self.config.get_remote_port()

        if remote_ip != self.current_remote_ip or remote_port != self.current_remote_port:
            self.create_udp_client(remote_ip, remote_port)

        msg = osc_message_builder.OscMessageBuilder(address=osc_address)
        for arg in osc_arguments:
            msg.add_arg(arg)
        osc_msg = msg.build()

        print(f"Send Data. Address: {osc_address}, Arguments: {osc_arguments}")
        self.client.send(osc_msg)
