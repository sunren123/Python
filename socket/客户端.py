import socket




def main():
    tcp_socket= socket.socket(socket.AD_INET, socket.SOCK_STREAM)

    tcp_socket.connect()


if __name__ == '__main__':
    main()
