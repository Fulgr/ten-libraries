import socket

def request(data):
    data = data.split(',')
    host = data[0]
    port = int(data[1])
    msg = ','.join(data[2:])
    msg = msg.replace('%', '\r\n')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(msg.encode())
    return s.recv(1024).decode()

def exec(data, q):
    if data == "q":
        return request(str(q))
    return False