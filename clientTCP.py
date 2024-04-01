import socket
import time
import matplotlib.pyplot as plt


# Configurações do servidor TCP
SERVER_IP = '192.168.0.10'
SERVER_PORT = 55555

# Função para enviar dados via TCP
def send_tcp(data):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((SERVER_IP, SERVER_PORT))
    tcp_socket.send(data)
    tcp_socket.close()

# Dados a serem enviados
data = b'x' * 1024  # 10 KB de dados

# Número de repetições do experimento
NUM_REPEATS = 30

# Medição para TCP
tcp_times = []
for _ in range(NUM_REPEATS):
    start_time = time.time()
    send_tcp(data)
    end_time = time.time()
    elapsed_time = end_time - start_time
    tcp_times.append(elapsed_time)

# Calcular taxas de transferência para TCP
tcp_throughputs = []
for t in tcp_times:
    if t != 0:
        throughput = len(data) / t
        tcp_throughputs.append(throughput)
    else:
        tcp_throughputs.append(0)

print("Taxas de transferência para TCP:")
for throughput in tcp_throughputs:
    print(f"Taxa de transferência: {throughput:.2f} bytes por segundo")
    
iterations = list(range(1, NUM_REPEATS + 1))
plt.plot(iterations, tcp_throughputs, label='UDP', color='red')
plt.xlabel('Iteração')
plt.ylabel('Taxa de Transferência (bytes por segundo)')
plt.show()