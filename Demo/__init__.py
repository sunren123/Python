import socket

def main():
    #socket.AD_INET 表示ipv4协议  socket.SOCK_STREAM 表示 tcp网络
    # s= socket.socket(socket.AD_INET, socket.SOCK_STREAM)

    #socket.AD_INET 表示ipv4协议  socket.SOCK_DGRAM 表示 udp网络
    #创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #链接服务器

    server_ip = input("请输入要链接的ip：")
    server_port = int(input("请输入要链接的port："))
    server_addr = (server_ip , server_port)
    tcp_socket.connect(server_addr)


    while True:
        #发送数据，接收数据

        send_data=input("请输入要发送的数据：")
        print("退出请输入：exit")
        if send_data == "exit":
            break

        tcp_socket.send(send_data.encode("gbk"))


    #关闭套接字
    tcp_socket.close()



if __name__ == '__main__':
   main()