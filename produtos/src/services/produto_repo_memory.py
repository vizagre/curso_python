from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict, Optional

from src.models.produto import Produto
from src.services.produto_repo_base import ProdutoRepositoryBase

class ProdutoRepositoryMemory(ProdutoRepositoryBase):
    """ Implementação da interface de repositório de produtos usando memória. """

    def __init__(self) -> None:
        self._produtos: Dict[int, Produto] = {}
        self._proximo_id: int = 1

    def listar(self) -> List[Produto]:
        return list(self._produtos.values())

    def buscar_por_id(self, id_: int) -> Optional[Produto]:
        return self._produtos.get(id_)
    
    def criar(self, nome: str, preco: float, ativo: bool) -> Produto:
        produto = Produto(id=self._proximo_id, nome=nome, preco=preco, ativo=ativo)
        self._produtos[self._proximo_id] = produto
        self._proximo_id += 1
        return produto

    def atualizar(self, id_: int, nome: str, preco: float, ativo: bool) -> Optional[Produto]:
        produto = self._produtos.get(id_)

        if not produto:
            return None

        produto.nome = nome
        produto.preco = preco
        produto.ativo = ativo
        
        return produto

    def remover(self, id_: int) -> bool:
        if id_ in self._produtos:
            del self._produtos[id_]
            return True
        return False

