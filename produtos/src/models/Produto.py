import datetime
from abc import abstractmethod, ABC

class Produto(ABC):
    """
        Classe que representa um produto.
    """

    def __init__(self, id: int, nome: str, preco: float, data_criacao: datetime.date, ativo: bool = True) -> None:
        self.id :int = id
        self.nome :str = nome
        self.preco :float  = preco
        self.data_criacao :datetime.date = data_criacao
        self.ativo :bool = ativo


    def __str__(self) -> str:
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco}, data_criacao={self.data_criacao}, ativo={self.ativo})" 
    

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


