from __future__ import annotations
import datetime
from typing import Optional
from pydantic import BaseModel, Field   


class ProdutoBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100,
                      description="O nome do produto deve ter entre 3 e 100 caracteres.")
    
    preco: float = Field(..., gt=0, 
                         description="O preço deve ser maior que zero.")
    
    sku: str = Field(..., min_length=3, max_length=50,
                     description="O SKU deve ter entre 3 e 50 caracteres.") 

    ativo: bool = True

    data_criacao: datetime.datetime = Field(default_factory=datetime.datetime.now)


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

    sku: Optional[str] = Field(None, min_length=3, max_length=50,
                             description="O SKU deve ter entre 3 e 50 caracteres.") 
    
    data_criacao: Optional[datetime.datetime] = None


class ProdutoRead(ProdutoBase):
    """ DTO para leitura de um produto (GET). """
    id: int

    class Config:
        from_attributes = True


