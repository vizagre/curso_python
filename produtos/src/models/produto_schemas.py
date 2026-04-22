from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field   


class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100,
                      description="O nome do produto deve ter entre 3 e 100 caracteres.")
    
    preco: float = Field(..., gt=0, 
                         description="O preço deve ser maior que zero.")
    
    ativo: bool = True


class ProdutoCreate(ProdutoBase):
    """ DTO para criação de um produto (POST). """
    pass


class ProdutoUpdate(BaseModel):
    """ DTO para atualização de um produto (PUT). """
    nome: Optional[str] = Field(None, min_length=3, max_length=100,
                                description="O nome do produto deve ter entre 3 e 100 caracteres.")
    
    preco: Optional[float] = Field(None, gt=0, 
                                  description="O preço deve ser maior que zero.")
    
    ativo: Optional[bool] = None


class ProdutoRead(ProdutoBase):
    """ DTO para leitura de um produto (GET). """
    id: int

    class Config:
        from_attributes = True


