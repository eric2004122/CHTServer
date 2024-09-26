import socket
import threading

# 設定伺服器的IP和端口
HOST = '127.0.0.1'
PORT = 12345

# 儲存所有連接的客戶端
clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"收到訊息: {message.decode('utf-8')}")
                broadcast(message, client_socket)
            else:
                clients.remove(client_socket)
                client_socket.close()
                break
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"伺服器啟動，等待連接...")

    while True:
        client_socket, client_address = server.accept()
        print(f"連接來自: {client_address}")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()    import socket
    import threading
    
    # 設定伺服器的IP和端口
    HOST = '127.0.0.1'
    PORT = 12345
    
    def receive_messages(client_socket):
        while True:
            try:
                message = client_socket.recv(1024)
                if message:
                    print(message.decode('utf-8'))
                else:
                    client_socket.close()
                    break
            except:
                client_socket.close()
                break
    
    def main():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
    
        thread = threading.Thread(target=receive_messages, args=(client_socket,))
        thread.start()
    
        while True:
            message = input()
            client_socket.send(message.encode('utf-8'))
    
    if __name__ == "__main__":
        main()