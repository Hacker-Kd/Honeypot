import socket


def honeypot():
    host = ''  # Listen on all interfaces
    port = 8888  # Choose a different port number

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)  # Listen for incoming connections
        print(f'Honeypot listening on port {port}...')

        while True:
            conn, addr = s.accept()
            print(f'Connection attempt from: {addr}')
            with conn:
                conn.sendall(b'Welcome to the honeypot!\n')


if __name__ == '__main__':
    honeypot()
