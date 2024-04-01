import socket


# Config do serve 
SERVER_IP = '192.168.0.10'
SERVER_PORT_TCP = 55555


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((SERVER_IP, SERVER_PORT_TCP))
tcp_socket.listen(1) 

print(f"Servidor TCP ouvindo em {SERVER_IP}:{SERVER_PORT_TCP}...")


def handle_tcp_connection(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Dados recebidos via TCP:", data.decode())
    conn.close()



while True:
    conn, addr = tcp_socket.accept()
    print(f"Conexão TCP estabelecida com {addr[0]}:{addr[1]}")
    handle_tcp_connection(conn)



