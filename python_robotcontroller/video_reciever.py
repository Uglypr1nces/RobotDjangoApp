import socket
import struct
import io
from PIL import Image
import matplotlib.pyplot as plt

def start_video_server():
    # Set up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.53', 5555))
    server_socket.listen(0)

    print("Waiting for connection...")

    # Accept client connection
    connection = server_socket.accept()[0].makefile('rb')

    try:
        img = None

        while True:
            # Read the length of the image as a 32-bit unsigned int. If the
            # length is zero, quit the loop
            image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                break

            # Construct a stream to hold the image data and read the image
            # data from the connection
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))

            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)

            # Display the image using matplotlib
            if img is None:
                plt.ion()  # Turn on interactive mode for real-time updating
                img = plt.imshow(image)
            else:
                img.set_data(image)

            plt.pause(0.01)
            plt.draw()

            print('Image is %dx%d' % image.size)
            # Optional: Verify the image
            # image.verify()
            # print('Image is verified')

    finally:
        connection.close()
        server_socket.close()
