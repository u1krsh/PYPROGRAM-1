import cv2
import socket
import struct
import numpy as np

server_ip = input("Enter server IP: ")
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))

data = b''
payload_size = struct.calcsize("!I")

try:
    while True:
        # Read frame length
        while len(data) < payload_size:
            packet = client_socket.recv(4096)
            if not packet:
                raise ConnectionError("No data received from server.")
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("!I", packed_msg_size)[0]

        # Read the actual frame data
        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('Client - Live Feed', frame)

        if cv2.waitKey(1) == 27:  # ESC to quit
            break
except Exception as e:
    print("Client Error:", e)
finally:
    client_socket.close()
    cv2.destroyAllWindows()
