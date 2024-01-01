from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import threading


class OSCReceiver:
    server_lock = threading.Lock()
    server = None
    current_local_ip = None
    current_local_port = None

    def __init__(self, config, received_params):
        self.config = config
        self.received_params = received_params

        self.dispatcher = Dispatcher()
        self.dispatcher.set_default_handler(self.osc_callback)

        self.run_server()
        self.config.register_config_change_callback(self.run_server)


    def run_server(self):
        thread = threading.Thread(target=self.run_server_async)
        thread.start()

    def run_server_async(self):
        local_ip, local_port = self.config.get_local_ip_and_port()
        print(f"{local_ip=} {local_port=} {self.current_local_ip=} {self.current_local_port=}")
        if local_ip == self.current_local_ip and local_port == self.current_local_port:
            return
        else:
            self.current_local_ip = local_ip
            self.current_local_port = local_port

        self.server_lock.acquire()

        server = None
        try:
            if self.server is not None:
                self.server.shutdown()
            server = BlockingOSCUDPServer((local_ip, local_port), self.dispatcher)
            self.server = server

            print(f"Listening for OSC messages on {local_ip}:{local_port}")
        except Exception as err:
            print(f"Failed to build the OSC receiver server. {err=}")
        finally:
            self.server_lock.release()

        if server is None:
            return
        
        server.serve_forever()
        print(f"OSC server shutting down. {local_ip}:{local_port}")


    def close(self):
        self.server_lock.acquire()

        if self.server is not None:
            self.server.shutdown()
            self.server = None

        self.server_lock.release()


    def osc_callback(self, address, *args):
        print(f"Received: {address=} {args=}")
        if len(args) > 0:
            self.received_params.add_received_param(address, args[0])
