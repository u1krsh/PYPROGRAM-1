import cv2
import socket
import struct

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host_ip = socket.gethostbyname(socket.gethostname())
port = 9999
server_socket.bind((host_ip, port))
server_socket.listen(1)
print(f"Server started at {host_ip}:{port}")

conn, addr = server_socket.accept()
print(f"Client connected: {addr}")

cap = cv2.VideoCapture(0)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]  # Lower = faster

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        result, img_encoded = cv2.imencode('.jpg', frame, encode_param)
        data = img_encoded.tobytes()

        # First send the length of the image, then the image
        conn.sendall(struct.pack("!I", len(data)) + data)
except Exception as e:
    print("Server Error:", e)
finally:
    cap.release()
    conn.close()
    server_socket.close()
