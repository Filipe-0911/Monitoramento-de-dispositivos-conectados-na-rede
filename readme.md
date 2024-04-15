# Sistema de Gestão de Acesso na Rede

Este projeto é um sistema de gestão de acesso à rede que permite inserir, listar, buscar, alterar e excluir dispositivos conectados à rede.

## Funcionalidades

- **Inserir Dispositivo:** Permite adicionar um novo dispositivo à lista de dispositivos gerenciados.
- **Listar Dispositivos:** Lista todos os dispositivos já inseridos no sistema.
- **Buscar Dispositivo Específico:** Permite encontrar um dispositivo específico pelo nome ou pelo endereço MAC.
- **Alterar Dispositivo:** Permite alterar o nome e o endereço MAC de um dispositivo existente.
- **Excluir Dispositivo:** Remove um dispositivo da lista.
- **Inserir Dispositivos em Série:** Realiza uma varredura na rede local e adiciona todos os dispositivos encontrados à lista.

## IMPORTANTE!
Antes de utilizar, crie um arquivo .env na pasta raiz com as seguintes variáveis:
- user=
- password=
- host=
- db_name=

Onde: user será o nome do usuário do banco de dados MySQL; password será a senha deste usuário MySQL; host será o endereço seguido da porta, ex.: localhost:3306; db_name será o nome do banco de dados do MySQL.

## Requisitos

- Python 3.x
- SQLAlchemy
- PyMySQL
- Dotenv

## Instalação e Uso

1. Clone o repositório:
git clone https://github.com/seu-usuario/Monitoramento-de-dispositivos-conectados-na-rede.git

2. Instale as dependências:

```
shell
pip install -r requirements.txt
```

3. Execute o arquivo principal:

```
shell
python app.py
```

Siga as instruções apresentadas no terminal para utilizar as funcionalidades do sistema.

## Estrutura do Projeto
O projeto está estruturado da seguinte forma:

- **app.py:** Arquivo principal que contém a lógica do programa.
- **src/controler/DispositivoController.py:** Controlador responsável por gerenciar as operações relacionadas aos dispositivos.
- **src/model/Dispositivo.py:** Modelo de dados que define a estrutura da tabela de dispositivos no banco de dados.
- **src/services/Leitura.py:** Serviço responsável pela leitura de dispositivos a partir de um arquivo.
- **requirements.txt:** Arquivo contendo as dependências necessárias para rodar o projeto.
- **README.md:** Este arquivo, contendo a documentação do projeto.