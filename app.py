from src.controler.DispositivoController import DispositivoController
from src.services.Leitura import Leitura
import subprocess
from src.services.Plataforma import Plataforma



def printa_opcoes():
    print()
    print("**********SISTEMA DE GESTÃO DE ACESSO NA REDE**********")
    print("Escolha uma das opções abaixo")
    print("0- Sair")
    print("1- Inserir dispositivo")
    print("2- Listar dispositivos já inseridos")
    print("3- Encontrar dispositivo específico (nome, mac address)")
    print("4- Alterar dispositivo a partir do ID")
    print("5- Excluir um dispositivo a partir de seu ID")
    print("6- Inserir dispositivos em série a partir de arquivo 'dispositivos_conectados.txt'")
    opcao = input("Escolha uma opção: ")
    print()
    return opcao

def main():
    sair = False
    
    while not sair:
        opcao = printa_opcoes()
        
        match(opcao):
            case "0": 
                sair = True
            case "1":
                nome = input("Digite o nome do dispositivo: ")
                mac = input("Digite o MAC Address do dispositivo: ")
                dispositivo = DispositivoController(nome, mac)
                
                print("Os dados estão corretos?")
                print("1- Sim")
                print("2- Não")
                print(dispositivo)
                confirma = input("-> ")
                                
                if confirma == "1":
                    verifica_se_ja_existe = dispositivo.consultar_especifico(mac=dispositivo.mac_address)
                    
                    if verifica_se_ja_existe:
                        print("Este dispositivo já está inserido no banco de dados")
                    else:
                        dispositivo.inserir_bd()
                else:
                    confirma = input("Qual dado você deseja alterar?")
                    print("1- Nome")
                    print("2- MAC Address")
                    
                    if confirma == "1":
                        novo_nome = input("Informe o nome corretamente: ")
                        print(novo_nome)
                        dispositivo.set_nome(novo_nome)
                        
                    if confirma == "2":
                        novo_mac_address = input("Informe o MAC Address corretamente: ")
                        print(novo_mac_address)
                        dispositivo.set_mac_address(novo_nome)
                    
                    print(DispositivoController.consultar_especifico(nome=dispositivo.nome))
                
            case "2":
                DispositivoController.consultar_dados()
            case "3":
                dispositivo = input("Informe o nome ou o MAC Address do dispositivo: ")
                if ":" in dispositivo:
                    print(DispositivoController.consultar_especifico(mac=dispositivo))
                else:
                    print(DispositivoController.consultar_especifico(nome=dispositivo))
                
            case "4":
                nome = input("Informe o novo nome: ")
                mac_address = input("Informe o novo MAC Address: ")
                id = int(input("Informe o ID do dispositivo: "))
                alteracao = DispositivoController(nome, mac_address)
                alteracao.alterar_dispositivo(id)
                
            case "5":
                DispositivoController.consultar_dados()
                print()
                id = int(input("Informe o ID do dispositivo que deseja EXCLUIR: "))
                print(f"Você confirma a EXCLUSÃO do Dispositivo com ID {id}?")
                print("1- Sim")
                print("2- Não")
                confirma = input("-> ")
                
                if confirma == "1":
                    try:
                        DispositivoController.remover_dispositivo(id)
                        print(f"Dispositivo removido com sucesso.")
                    except Exception as e:
                        print(f"Ocorreu um erro: {e}")
            
            case "6":
                try:
                    system = Plataforma().sistema.lower()
                    print(system)
                    comando = "sudo nmap -sn 192.168.1.0/24 > dispositivos_conectados.txt" if system != "windows" else "C:\\Program Files (x86)\\Nmap\\nmap.exe -sn 192.168.1.0/24 > dispositivos_conectados.txt"
                    subprocess.run(comando, shell=True, check=True)
                    
                    print("Comando executado com sucesso!")
                    
                except subprocess.CalledProcessError as e:
                    print("Erro ao executar o comando:", e)
                    
                leitura_arquivo = Leitura("dispositivos_conectados.txt")
                for disp in leitura_arquivo.get_conteudo():
                    dispositivo = DispositivoController(disp['nome'], disp['mac_address'])
                    verifica_se_ja_existe = dispositivo.consultar_especifico(mac=dispositivo.mac_address)
                        
                    if verifica_se_ja_existe:
                        print("Este dispositivo já está inserido no banco de dados")
                    else:
                        dispositivo.inserir_bd()     
                        
            case _:
                print("opcao inválida! Escolha novamente")

if __name__ == "__main__":
    main()