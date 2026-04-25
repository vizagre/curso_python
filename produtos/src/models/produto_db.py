from __future__ import annotations
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProdutoDB(Base):
    """
    Modelo ORM que representa a tabela de produtos no banco de dados usando SQLAlchemy.
    """

    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    sku = Column(String(255), nullable=False, unique=True)
    preco = Column(Float, nullable=False)
    data_criacao = Column(DateTime, nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"<ProdutoDB(id={self.id}, nome='{self.nome}', sku='{self.sku}', preco={self.preco}, data_criacao={self.data_criacao}, ativo={self.ativo})>" 
    
