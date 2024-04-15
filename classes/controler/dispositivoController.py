from classes.model.Dispositivo import Dispositivo
import datetime

class Dispositivos:
    Dispositivo.criar_tabela()
    dispositivo = Dispositivo()
    
    def __init__(self, nome=None, mac_address=None) -> None:
        self.__nome = nome.title()
        self.__mac_address = mac_address.lower()
        
    def __str__(self):
        return f"Nome:{self.__nome}, MAC Address:{self.__mac_address}"
    
    def __eq__(self, other):
        return self.__mac_address == other.__mac_address
    
    def set_nome(self, nome):
        self.__nome = nome
        
    def set_mac_address(self, mac):
        self.__mac_address = mac
        
    def detalhar(self):
        return self.__dict__
    
    def alterar_dispositivo(self, id):
        Dispositivos.__get_dispositivo().alterar_dispositivo(id, self)
    
    def inserir_bd(self):
        Dispositivos.__get_dispositivo().criar_dispositivo(nome=self.__nome, mac=self.__mac_address, data_acesso=datetime.datetime.now())
        
        return Dispositivos.__get_dispositivo().consultar_dispositivo(self.mac_address)
    
    @staticmethod
    def remover_dispositivo(id):
        try:
            Dispositivos.__get_dispositivo().remover_dispositivo(id)
        except Exception as e:
            print(e)
        
    @property
    def mac_address(self):
        return self.__mac_address
    
    @property
    def nome(self):
        return self.__nome
    
    @staticmethod
    def consultar_dados():
        
        lista = Dispositivos.dispositivo.consultar_dados()
        
        for disp in lista:
            print(disp)
        
    @staticmethod
    def consultar_especifico(nome=None, mac=None, id=None):   
        if nome:
            print()
            print(f"Nome: {nome}")
            return Dispositivos.__get_dispositivo().consultar_dispositivo(nome = nome)
        elif mac:
            print()
            print(f"mac: {mac}")
            return Dispositivos.__get_dispositivo().consultar_dispositivo(mac = mac)
        else:
            print()
            print(f"id: {id}")
            return Dispositivos.__get_dispositivo().consultar_dispositivo(id = id)
    
    @classmethod
    def __get_dispositivo(cls):
        return cls.dispositivo