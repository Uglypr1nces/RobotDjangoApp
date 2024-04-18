import socket

def client(usercommand, server, port):
    ADDR = (server, port)
    HEADER = 64
    FORMAT = "utf-8"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(ADDR)
    except ConnectionRefusedError:
        print("Connection refused: The server is not accepting connections.")
        return
    except TimeoutError:
        print("Connection timeout: The connection attempt timed out.")
        return
    except Exception as e:
        print(f"Connection error: {e}")
        return

    def send(msg):
        try:
            message = msg.encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b" " * (HEADER - len(send_length))

            client.send(send_length)
            client.send(message)
        except BrokenPipeError:
            print("Broken pipe: The connection was unexpectedly closed by the server.")
        except ConnectionResetError:
            print("Connection reset: The connection was reset by the server.")
        except OSError as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    send(usercommand)
