from __future__ import annotations
from datetime import datetime

class Produto:
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
        self._id: int = id_
        self.nome: str = nome
        self._sku: str = ""
        self.sku = sku
        self._preco: float = 0.00
        self.preco = preco
        self._data_criacao: datetime = datetime.now()
        self.data_criacao = data_criacao if data_criacao else datetime.now()
        self.ativo: bool = ativo


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

    @sku.setter
    def sku(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("O SKU não pode ser vazio.")
        self._sku = valor.strip()

    @data_criacao.setter
    def data_criacao(self, valor: datetime) -> None:
        if not isinstance(valor, datetime):
            raise ValueError("A data de criação deve ser um objeto datetime.")
        self._data_criacao = valor

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

