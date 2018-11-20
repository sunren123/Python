import socket
import re

def service_client(new_socket):
    #为这个客户端返回数据
    request = new_socket.recv(1024).decode("utf-8")


    print(request)
    #接收浏览器发送来的请求



    response ="HTTP/1.1 200 OK\r\n"
    response += "\r\n"

    #准备发送给浏览器的数据

    f = open("./html/index.html" , "rb")
    html_content=f.read()
    f.close()


    new_socket.send(response.encode("utf-8"))
    new_socket.send(html_content)

    #关闭套接字
    new_socket.close()

def main():
    #创建套接字
    tcp_server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #绑定
    tcp_server_socket.bind(("",7890))
    #变为监听套接字
    tcp_server_socket.listen(128)
    #等待新的客户端来链接

    while True:
        new_socker,client_addr=tcp_server_socket.accept()
        #为这个客服服务
        service_client(new_socker)

    #关闭套接字
    tcp_server_socket.close()
if __name__ == '__main__':
    main()