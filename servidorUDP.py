import socket

# Config do serve 
SERVER_IP = '192.168.0.10'
SERVER_PORT_UDP = 55556


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((SERVER_IP, SERVER_PORT_UDP))

print(f"Servidor UDP ouvindo em {SERVER_IP}:{SERVER_PORT_UDP}...")

# Função para tratar conexões UDP
def handle_udp_connection():
    while True:
        data, addr = udp_socket.recvfrom(61440) #bytes da mensagem , se for maior que isso n vai rodar  (60 KB)
        print("Dados recebidos via UDP:", data.decode())


handle_udp_connection()
