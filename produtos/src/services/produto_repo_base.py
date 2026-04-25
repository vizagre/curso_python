from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

try:
    from src.models.produto import Produto
except ModuleNotFoundError:
    from models.produto import Produto


class ProdutoRepositoryBase(ABC):
    """ Interface base para o repositório de produtos. """

    @abstractmethod
    def listar(self) -> List[Produto]:
        """ Retorna uma lista de todos os produtos. """
        raise NotImplementedError("O método listar() deve ser implementado na classe filha.")
    
    @abstractmethod
    def buscar_por_id(self, id_:int) -> Optional[Produto]:
        """ Retorna um produto pelo seu ID. """
        raise NotImplementedError("O método buscar_por_id() deve ser implementado na classe filha.")  
    
    @abstractmethod
    def buscar_por_sku(self, sku:str) -> Optional[Produto]:
        """ Retorna um produto pelo seu SKU. """
        raise NotImplementedError("O método buscar_por_sku() deve ser implementado na classe filha.")

    @abstractmethod
    def criar(self, nome:str, preco:float, sku:str, data_criacao:datetime, ativo:bool = True) -> Produto:
        """ Cria um novo produto e retorna o produto criado. """
        raise NotImplementedError("O método criar() deve ser implementado na classe filha.")
    
    @abstractmethod
    def atualizar(self, id_:int, nome:str, preco:float, sku:str, ativo:bool) -> Optional[Produto]:
        """ Atualiza um produto existente e retorna o produto atualizado. """
        raise NotImplementedError("O método atualizar() deve ser implementado na classe filha.")    
    
    @abstractmethod
    def remover(self, id_: int) -> bool:
        """ Remove um produto pelo seu ID. Retorna True se a remoção foi bem-sucedida, False caso contrário. """
        raise NotImplementedError("O método remover() deve ser implementado na classe filha.")  
    
