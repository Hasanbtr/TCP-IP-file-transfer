import socket

def start_server():
    # Sunucu IP adresi ve port numarası
    host = "127.0.0.1"
    port = 12345

    # TCP soketi oluştur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    # Bağlantıları dinle
    server_socket.listen()

    print(f"Sunucu dinlemede. IP: {host}, Port: {port}")

    # İstemci bağlantısını kabul et
    client_socket, client_address = server_socket.accept()
    print(f"Bağlantı kabul edildi. İstemci IP: {client_address[0]}, Port: {client_address[1]}")

    # Dosya adını al
    file_name = client_socket.recv(1024).decode("utf-8")
    print(f"Alınacak dosya adı: {file_name}")

    # Dosyayı aç ve içeriği al
    with open(file_name, "wb") as file:
        data = client_socket.recv(1024)
        while data:
            file.write(data)
            data = client_socket.recv(1024)

    print("Dosya başarıyla alındı.")
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
