from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.models.produto_db import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/produtos.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

def criar_tabelas() -> None:
    """ Função para criar as tabelas no banco de dados. """
    Base.metadata.create_all(bind=engine)


def get_db():
    """ Função para obter uma sessão de banco de dados. """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  
