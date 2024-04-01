import socket
import time
import matplotlib.pyplot as plt


# Configurações do servidor UDP
SERVER_IP = '192.168.0.10'
SERVER_PORT = 55556

# Tamanho das mensagens pela qual vamos usar 1KB 10KB ...
data_sizes = [1, 10, 20, 30, 40, 50, 60]
data_sizes_bytes = [size * 1024 for size in data_sizes]  # Converte pra bytes 

def send_udp(data):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(data, (SERVER_IP, SERVER_PORT))
    udp_socket.close()

# Dicionário que armazenar as taxas de transferências 
transfer_rates_udp = {}

# Número de repetições , ex: 100 mensagens de 1KB... e assim vai
NUM_REPEATS = 100



for data_size_bytes in data_sizes_bytes:
    
    data = b'x' * data_size_bytes # mensagem que vai ser enviada 
    
    # Lista para armazenar as taxas de transferência de dados
    udp_throughputs = []
    
    for _ in range(NUM_REPEATS):
        start_time = time.time()
        send_udp(data)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # Calcular a taxa de transferência 
        if elapsed_time != 0:
            throughput = len(data) / elapsed_time
            udp_throughputs.append(throughput)
        else:
            udp_throughputs.append(0)
    
    # Calcular a média das taxas de transferência
    average_throughput = sum(udp_throughputs) / len(udp_throughputs)
    
    # Armazenar a média das taxas de transferência 
    transfer_rates_udp[data_size_bytes] = average_throughput

    print(f"Média de taxa de transferência para {data_size_bytes / 1024} KB: {average_throughput:.2f} bytes por segundo")

# Graficos UDP
plt.bar([data_size_bytes / 1024 for data_size_bytes in transfer_rates_udp.keys()], transfer_rates_udp.values(), color='blue')
plt.xlabel('Tamanho dos Dados (KB)')
plt.ylabel('Taxa de Transferência Média (bytes por segundo)')
plt.title('Taxa de Transferência Média UDP para Diferentes Tamanhos de Dados')
plt.show()

#MODIFIQUEI PARA O CODIGO ORIGINAL  , AQUELE FOI SÓ PARA PEGAR O TEMPO.
