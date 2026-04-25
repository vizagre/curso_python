from __future__ import annotations
from typing import List, Optional
from datetime import datetime

from sqlalchemy.orm import Session

from src.models.produto import Produto  
from src.models.produto_db import ProdutoDB
from src.services.produto_repo_base import ProdutoRepositoryBase    

class ProdutoRepositorySQLAlchemy(ProdutoRepositoryBase):
    """ Implementação da interface de repositório de produtos usando SQLAlchemy. """

    def __init__(self, db: Session) -> None:
        self._db = db

    # Método auxiliar para converter ProdutoDB em Produto
    def _db_to_entity(self, produto_db: ProdutoDB) -> Produto:
        return Produto(
            id_=produto_db.id,
            nome=produto_db.nome,
            preco=produto_db.preco,
            sku=produto_db.sku,
            data_criacao=produto_db.data_criacao,
            ativo=produto_db.ativo
        )
    
    # Listar todos os produtos
    def listar(self) -> List[Produto]:
        produtos_db = self._db.query(ProdutoDB).all()
        return [self._db_to_entity(p) for p in produtos_db]


    # Buscar produto por ID
    def buscar_por_id(self, id_: int) -> Optional[Produto]:
        produto_db = self._db.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        if produto_db:
            return self._db_to_entity(produto_db)
        return None
    

    # Buscar produto por SKU
    def buscar_por_sku(self, sku: str) -> Optional[Produto]:
        produto_db = self._db.query(ProdutoDB).filter(ProdutoDB.sku == sku).first()
        if produto_db:
            return self._db_to_entity(produto_db)
        return None
    

    # Criar um novo produto
    def criar(self, nome: str, preco: float, sku: str, data_criacao: datetime, ativo: bool) -> Produto:
        novo_produto_db = ProdutoDB(nome=nome, preco=preco, sku=sku, data_criacao=data_criacao, ativo=ativo)
        self._db.add(novo_produto_db)
        self._db.commit()
        self._db.refresh(novo_produto_db)
        return self._db_to_entity(novo_produto_db)


    # Atualizar um produto existente
    def atualizar(self, id_: int, nome: str, preco: float, sku: str, ativo: bool) -> Optional[Produto]:
        produto_db = self._db.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        if not produto_db:
            return None
        produto_db.nome = nome
        produto_db.preco = preco
        produto_db.sku = sku
        produto_db.ativo = ativo
        self._db.commit()
        self._db.refresh(produto_db)
        return self._db_to_entity(produto_db)   
    
    # Remover um produto
    def remover(self, id_: int) -> bool:
        produto_db = self._db.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        if not produto_db:
            return False
        self._db.delete(produto_db)
        self._db.commit()
        return True
    
    