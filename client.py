import socket

def start_client():
    # Sunucu IP adresi ve port numarası
    host = "127.0.0.1"
    port = 12345

    # TCP soketi oluştur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Sunucuya bağlan
    client_socket.connect((host, port))
    print(f"Sunucuya bağlandı. IP: {host}, Port: {port}")

    # Gönderilecek dosya adını belirt
    file_name = "example.txt"
    client_socket.send(file_name.encode("utf-8"))

    # Dosyayı aç ve içeriği gönder
    with open(file_name, "rb") as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

    print("Dosya başarıyla gönderildi.")
    client_socket.close()

if __name__ == "__main__":
    start_client()
