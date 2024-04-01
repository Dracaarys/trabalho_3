import socket
import time
import matplotlib.pyplot as plt


# Configurações do servidor UDP
SERVER_IP = '192.168.0.10'
SERVER_PORT = 55556

# Função de enviados dados UDP
def send_udp(data):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(data, (SERVER_IP, SERVER_PORT))
    udp_socket.close()

# Dados a serem enviados / alterar aqui para fazer os testes 10KB , 20KB ...
data = b'x'  * 1024  # 1 KB de dados

# Número de repetições do experimento
NUM_REPEATS = 30

# Medição para UDP
udp_times = []
for _ in range(NUM_REPEATS):
    start_time = time.time()
    send_udp(data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    udp_times.append(elapsed_time)

# Calcular taxas de transferência para UDP
udp_throughputs = []
for t in udp_times:
    if t != 0:
        throughput = len(data) / t
        udp_throughputs.append(throughput)
    else:
        udp_throughputs.append(0)

print("\nTaxas de transferência para UDP:")
for throughput in udp_throughputs:
    print(f"Taxa de transferência: {throughput:.2f} bytes por segundo")

iterations = list(range(1, NUM_REPEATS + 1))
plt.plot(iterations, udp_throughputs, label='UDP', color='blue')
plt.xlabel('Iteração')
plt.ylabel('Taxa de Transferência (bytes por segundo)')
plt.show()