from __future__ import annotations
from datetime import datetime

class Produto():
    """
        Classe que representa um produto.
        Atributos:
            id (int): O identificador único do produto.
                id_ -> parâmetro do construtor
                _id -> atributo privado

            nome (str): O nome do produto.
            preco (float): O preço do produto.
                _preco -> atributo privado
            data_criacao (datetime): A data e hora em que o produto foi criado.
            ativo (bool): Indica se o produto está ativo ou não.
    """

    def __init__(self, id_: int, nome: str, sku: str, preco: float, data_criacao: datetime = None, ativo: bool = True) -> None:
        self._id :int = id_
        self.nome :str = nome
        self.sku :str = sku
        self._preco :float  = 0.00
        self.preco = preco
        self.data_criacao :datetime = data_criacao if data_criacao else datetime.now()
        self.ativo :bool = ativo


    def __str__(self) -> str:
        return f"Produto(id={self._id}, nome='{self.nome}', sku='{self._sku}', preco={self._preco}, data_criacao={self.data_criacao}, ativo={self.ativo})" 


    @property
    def id(self) -> int:   
        return self._id

    @property
    def sku(self) -> str:
        return self._sku

    @property
    def preco(self) -> float:
        return self._preco

    @property
    def data_criacao(self) -> datetime:
        return self._data_criacao   

    @property
    def sku(self) -> str:
        return self._sku

    @preco.setter
    def preco(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor


    def aplicar_desconto(self, percentual: float) -> None:
        """
            Aplica um desconto ao preço do produto.
                :param percentual: O percentual de desconto a ser aplicado (entre 0 e 100).
                :raises ValueError: Se o percentual de desconto for inválido.
        """
        if percentual <= 0 or percentual >= 100:
            raise ValueError("O percentual de desconto deve ser entre 0 e 100.")
        
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto


    def ativar(self) -> None:
        """Ativa o produto."""
        self.ativo = True   


    def desativar(self) -> None:
        """Desativa o produto."""
        self.ativo = False      

