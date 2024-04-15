from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, VARCHAR
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()
engine = create_engine(f'mysql+pymysql://{os.environ['user']}:{os.environ["password"]}@{os.environ["host"]}/{os.environ["db_name"]}')
Session = sessionmaker(bind=engine)
session = Session()

class Dispositivo(Base):
    __tablename__ = "Dispositivos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(VARCHAR(length=60))
    mac = Column(VARCHAR(length=60))
    data_acesso = Column(Date)
    
    @staticmethod
    def criar_tabela():
        Base.metadata.create_all(engine)

    def criar_dispositivo(self, nome, mac, data_acesso):

        new_dispositivo = Dispositivo(nome=nome, mac=mac, data_acesso=data_acesso)
        session.add(new_dispositivo)
        session.commit()
        session.close()

    def consultar_dados(self):
        # Consultar dados
        dispositivos = session.query(Dispositivo).all()
        session.close()
        return dispositivos
    
    def consultar_dispositivo(self, nome = None, mac = None, id = None):
        if nome:
            dispositivo = session.query(Dispositivo).filter(Dispositivo.nome==nome).first()
        elif mac:
            dispositivo = session.query(Dispositivo).filter(Dispositivo.mac==mac).first()
        else:
            dispositivo = session.query(Dispositivo).filter(Dispositivo.id==id).first()
        
        session.close()
        
        return dispositivo
    
    def consultar_por_data(self, data):
        data_formatada = datetime.datetime.strptime(data, '%Y-%m-%d')
        lista = session.query(Dispositivo).all()
        
        session.close()
        return list(filter(lambda disp: disp.data_acesso == data_formatada.date(), lista))
    
    def alterar_dispositivo(self, id, object):
        session.query(Dispositivo).filter(Dispositivo.id == id).update(
            {"nome": object.nome, "mac": object.mac_address}, synchronize_session="fetch"
        )
        
        session.commit()
    
    def remover_dispositivo(self, id):
        session.query(Dispositivo).filter(Dispositivo.id == id).delete()
        session.commit()
        
        return session.query(Dispositivo).all()
    
    def __str__(self):
        data = self.data_acesso.strftime("%d/%m/%Y")
        return f"id: {self.id}; Dispositivo: {self.nome}; MAC Address: {self.mac}; Data de acesso: {data}"
    
    def detalhar(self):
        return self.__dict__