import nmap

# Crie um objeto nmap.PortScanner
scanner = nmap.PortScanner()


# Execute a varredura de hosts
scanner.scan(hosts='192.168.1.0/24', arguments='-sn')

# Obtenha a saída da varredura
output = scanner.get_nmap_last_output()

# Escreva a saída no arquivo
with open('dispositivos_conectados.txt', 'w') as f:
    f.write(output)
