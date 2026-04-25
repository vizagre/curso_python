from __future__ import annotations
from typing import List, Dict, Optional
from datetime import datetime

try:
    from src.models.produto import Produto
    from src.services.produto_repo_base import ProdutoRepositoryBase
except ModuleNotFoundError:
    from models.produto import Produto
    from services.produto_repo_base import ProdutoRepositoryBase

class ProdutoRepositoryMemory(ProdutoRepositoryBase):
    """ Implementação da interface de repositório de produtos usando memória. """

    def __init__(self) -> None:
        self._produtos: Dict[int, Produto] = {}
        self._proximo_id: int = 1

    def listar(self) -> List[Produto]:
        return list(self._produtos.values())

    def buscar_por_id(self, id_: int) -> Optional[Produto]:
        return self._produtos.get(id_)
    
    def buscar_por_sku(self, sku: str) -> Optional[Produto]:
        for produto in self._produtos.values():
            if produto.sku == sku:
                return produto
        return None
    
    def criar(self, nome: str, preco: float, sku: str, data_criacao: datetime, ativo: bool) -> Produto:
        produto = Produto(id_=self._proximo_id, nome=nome, preco=preco, sku=sku, data_criacao=data_criacao, ativo=ativo)
        self._produtos[self._proximo_id] = produto
        self._proximo_id += 1
        return produto

    def atualizar(self, id_: int, nome: str, preco: float, sku: str, ativo: bool) -> Optional[Produto]:
        produto = self._produtos.get(id_)

        if not produto:
            return None

        produto.nome = nome
        produto.preco = preco
        produto.sku = sku
        produto.ativo = ativo
        return produto

    def remover(self, id_: int) -> bool:
        if id_ in self._produtos:
            del self._produtos[id_]
            return True
        return False

