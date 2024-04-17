import socket

socket_client = socket.socket()
socket_client.connect(("localhost", 8886))
while True:
    msg = input("请输入发送给服务端的消息")
    if msg == "exit":
        break
    socket_client.send(msg.encode("UTF-8"))
    data = socket_client.recv(1024).decode("UTF-8")
    print(f"服务端回复的消息是{data}")
socket_client.close()
