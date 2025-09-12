from socket import *
import threading

PORT = 26027


# -----------------------------------------------------------------------------
# starts server
# -----------------------------------------------------------------------------
def server_start():
    # SOCK_DGRAM = UDP
    server = socket(AF_INET, SOCK_DGRAM)
    server.bind(('127.0.0.1', PORT))
    return server


# -----------------------------------------------------------------------------
# accepts connections from clients
# -----------------------------------------------------------------------------
def server_accept(server):

    while True:
        # Pour les sockets UDP, pas de connection "handshake"
        # pas de contrôle des paquets, on utilise directement
        # recvfrom sans accept
        s_data, client = server.recvfrom(1024)
        if s_data == b'quit':
            break
        if s_data != b'':
            _str = s_data.decode('utf-8')
            print(f"server : {_str}")
        # en UDP, on utilise sendto au lieu de send ou sendall
        server.sendto(bytes(_str[::-1], 'utf-8'), client)

    server.close()


# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == '__main__':

    print('Simple server implementation')
    server = server_start()
    thread = threading.Thread(target=server_accept, args=(server,))
    thread.start()

    with socket(AF_INET, SOCK_DGRAM) as sock:
        sock.sendto(b'These are my data\nEnd.', ('127.0.0.1', PORT))
        data = sock.recvfrom(1024)
        print(f"client : {data[0].decode('utf-8')}")
        sock.sendto(b'quit', ('127.0.0.1', PORT))



