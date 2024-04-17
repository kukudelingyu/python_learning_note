import socket

# 创建socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost", 8886))
# 监听端口，back_log:允许的链接数量
socket_server.listen(1)
# 等待客户端连接, 返回二元元组, accept是（阻塞方法）
print("服务端已启动：")
result = socket_server.accept()
conn = result[0]    #客户端和服务端的连接对象
address = result[1] #客户端的地址信息
# conn, address = socket_server.accept()
print(f"接收到了客户端的连接信息，客户端地址为{address}")
# 接收客户端的信息，要使用客户端和服务端的连接对象，而不是socket_server，recv的参数是缓冲区大小, 返回的对象是一个字节数组，通过decode转为字符串
while True:
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的消息是：{data}")
    msg = input("你要回复客户端的消息是：")
    if msg == "exit":
        break
    conn.send(msg.encode("UTF-8"))
# 关闭连接
conn.close()
socket_server.close()
