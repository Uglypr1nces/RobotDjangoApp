import socket

def client(usercommand, server, port):

    ADDR = (server, port)
    HEADER = 64
    FORMAT = "utf-8"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b" " * (HEADER - len(send_length))
        try:

            client.send(send_length)
            client.send(message)
        except ConnectionResetError:
            print(f"Connection with {addr} was forcibly closed.")
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    send(usercommand)
