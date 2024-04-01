import socket
import time
import matplotlib.pyplot as plt

# Configurações do servidor TCP
SERVER_IP = '192.168.0.10'
SERVER_PORT = 55555

# Tamanho das mensagens pelas quais vamos usar 1KB, 10KB, ...
data_sizes = [1, 10, 20, 30, 40, 50, 60]
data_sizes_bytes = [size * 1024 for size in data_sizes]  # Convertendo para bytes

def send_tcp(data):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((SERVER_IP, SERVER_PORT))
    tcp_socket.send(data)
    tcp_socket.close()

# Dicionário para armazenar as taxas de transferências 
transfer_rates_tcp = {}

# Número de repetições, ex: 100 mensagens de 1KB... e assim vai
NUM_REPEATS = 100

# Lista para armazenar os tempos de execução
execution_times = []

# Marcação de tempo inicial
start_total_time = time.time()

for data_size_bytes in data_sizes_bytes:
    
    data = b'a' * data_size_bytes  # Mensagem que será enviada 
    
    # Lista para armazenar as taxas de transferência de dados
    tcp_throughputs = []
    
    # Marcação de tempo 
    start_time = time.time()
    
    for _ in range(NUM_REPEATS):
        send_tcp(data)
    
    # Marcação de tempo final para este tamanho de dados
    end_time = time.time()
    
    # Calcular o tempo de execução para este tamanho de dados
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    
    # Calcular a média das taxas de transferência para este tamanho de dados
    average_throughput = data_size_bytes * NUM_REPEATS / execution_time
    
    # Armazenar a média das taxas de transferência 
    transfer_rates_tcp[data_size_bytes] = average_throughput

    print(f"Média de taxa de transferência para {data_size_bytes / 1024} KB: {average_throughput:.2f} bytes por segundo")

end_total_time = time.time()

# Calcular o tempo de execução
total_execution_time = end_total_time - start_total_time

print(f"Tempo total de execução: {total_execution_time:.2f} segundos")

# Plotar o gráfico de tempo de execução
plt.plot([data_size_bytes / 1024 for data_size_bytes in data_sizes_bytes], execution_times, marker='o', color='orange')
plt.xlabel('Tamanho dos Dados (KB)')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução TCP para Diferentes Tamanhos de Dados')
plt.show()


# MUDEI O CODIGO PARA PEGAR O TEMPO E VER OUTROS GRAFICOS. A TAXA DE TRANSFERENCIA ESTA NA IMAGEM E NO TERMINAL.