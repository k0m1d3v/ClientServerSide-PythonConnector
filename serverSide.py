import socket

host = "0.0.0.0"
port = 4444
bufferSize = 8000


def server():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((host, port))
    connection.listen(1)
    conn, add = connection.accept()
    print(f"connection by {add}")


if __name__ == "__main__":
    server()
