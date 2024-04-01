import socket

# Configurações do servidor UDP
SERVER_IP = '192.168.0.10'
SERVER_PORT_UDP = 55556

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((SERVER_IP, SERVER_PORT_UDP))

print(f"Servidor UDP ouvindo em {SERVER_IP}:{SERVER_PORT_UDP}...")

# Função para tratar conexões UDP
def handle_udp_connection():
    while True:
        data, addr = udp_socket.recvfrom(1024)# Recebe dados de 1024 bytes(alterar quando mudar "dados a serem enviados")
        print("Dados recebidos via UDP:", data.decode())

# Tratamento de conexões UDP
handle_udp_connection()
