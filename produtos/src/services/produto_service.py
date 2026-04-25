from __future__ import annotations
from datetime import datetime
from typing import List, Optional

try:
    from src.models.produto import Produto
    from src.services.produto_repo_base import ProdutoRepositoryBase
except ModuleNotFoundError:
    from models.produto import Produto
    from services.produto_repo_base import ProdutoRepositoryBase

class ProdutoService:

    """
    Service class for managing products.
    """

    def __init__(self, repo: ProdutoRepositoryBase) -> None:
        self._repo = repo


    def listar_produto(self) -> List[Produto]:
        """
        List all products.
        """
        return self._repo.listar()
    

    def obter_produto(self, id_: int) -> Optional[Produto]:
        """
        Get a product by its ID.
        """
        return self._repo.buscar_por_id(id_) 
    

    def obter_produto_por_sku(self, sku: str) -> Optional[Produto]:
        """
        Get a product by its SKU.
        """
        return self._repo.buscar_por_sku(sku)
    

    def criar_produto(self, nome: str, preco: float, sku: str, data_criacao: datetime, ativo: bool):
        return  self._repo.criar(nome, preco, sku, data_criacao, ativo)


    def atualizar_produto(self, id_: int, nome: str, preco: float, sku: str, ativo: bool) -> Optional[Produto]:
        """
        Update a product by its ID.
        """
        return self._repo.atualizar(id_ = id_, nome = nome, preco = preco, sku = sku, ativo = ativo)
    

    def remover_produto(self, id_: int) -> bool:
        """
        Delete a product by its ID.
        """
        return self._repo.remover(id_)  
    
