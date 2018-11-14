import socket

def main():
    #socket.AD_INET 表示ipv4协议  socket.SOCK_STREAM 表示 udp网络
    s= socket.socket(socket.AD_INET, socket.SOCK_STREAM)

    #socket.AD_INET 表示ipv4协议  socket.SOCK_DGRAM 表示 tcp网络
    # s= socket.socket(socket.AD_INET, socket.SOCK_DGRAM)
    # s.send(b"人生苦短，我用Python",("192.168.1.102", 8080))

    while True:
        send_data= input("请输入你要输入的数据：")
        if send_data == "exit":
            break
        s.send(send_data.encode("utf-8"),("192.168.1.102", 8080))



    s.close()






if __name__ == '__main__':
   main()