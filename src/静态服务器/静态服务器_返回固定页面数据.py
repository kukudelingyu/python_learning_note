# 1.编写一个TCP服务端程序
# 2.获取浏览器发送的HTTP请求报文数据
# 3.读取固定的页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器
# 4.HTTP响应报文发送完成后，关闭服务于客户端的套接字
# 5.获取用户的请求资源路径
# 6.根据请求资源路径，读取指定的文件数据
# 7.组装指定文件数据的响应报文，发送给浏览器
# 8.判断请求的文件在服务端是否存在，组装404状态的响应报文发送给浏览器
import socket

if __name__ == '__main__':
    # 创建socket，设置ivp4
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定socket
    tcp_server_socket.bind(("",8081))
    # 设置监听
    tcp_server_socket.listen(128)
    while True:
        # 获取客户端socket和地址
        tcp_client_socket, address = tcp_server_socket.accept()
        print(f"客户端地址为：{address}")
        # 获取客户端请求信息
        client_request_data = tcp_client_socket.recv(1024).decode()
        request_path = client_request_data.split(" ")[1]
        print(f"path={request_path}")
        if request_path == "/":
            request_path = "/login.html"

        try:
            with open(f"."+request_path, "rb") as file:
                file_data = file.read()
                response_line = "HTTP/1.1 200 OK\r\n"
                response_header = "Server:pwb\r\n"
                response_body = file_data
                response_data = (response_line + response_header + "\r\n").encode() + response_body
                tcp_client_socket.send(response_data)

        except Exception as e:
            print(e)
            # 返回404错误数据
            with open("404.html", "rb") as f:
                f_data = f.read()
                response_line1 = "HTTP/1.1 404 OK\r\n"
                response_header1 = "Server:pwb\r\n"
                response_body1 = f_data
                response_data1 = (response_line1 + response_header1 + "\r\n").encode() + response_body1
                tcp_client_socket.send(response_data1)
        finally:
            tcp_client_socket.close()
