import socket

class RobotClient:
    def __init__ (self, server, port):
        self.ADDR = (server, port)
        self.HEADER = 64
        self.FORMAT = "utf-8"

    def connect(self):
        self.client.connect(self.ADDR)

    def set_server(self, server, port):
        self.ADDR = (server, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server set to", server, "on port", port)

    def listen(self):
        while True:
            try:
                msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = self.client.recv(msg_length).decode(self.FORMAT)
                    print(f"[{self.ADDR}] {msg}")
            except ConnectionResetError:
                print(f"Connection with {self.ADDR} was forcibly closed.")
            except socket.error as e:
                print(f"Socket error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def send_message(self,msg):
        if self.ADDR == "":
            print("No server set.")
        else:
            message = msg.encode(self.FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(self.FORMAT)
            send_length += b" " * (self.HEADER - len(send_length))
            try:
                self.client.send(send_length)
                self.client.send(message)
            except ConnectionResetError:
                print(f"Connection with {self.ADDR} was forcibly closed.")
            except socket.error as e:
                print(f"Socket error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
