from __future__ import annotations  
from typing import List
from fastapi import FastAPI, HTTPException, status

from src.models.produto_schemas import ProdutoCreate, ProdutoRead, ProdutoUpdate
from src.services.produto_repo_memory import ProdutoRepositoryMemory
from src.services.produto_service import ProdutoService


app = FastAPI(
    title="API de Produtos",
    description="Uma API para gerenciar produtos usando FastAPI e um repositório em memória.",
    version="1.0.0"
)

repo = ProdutoRepositoryMemory()
produto_service = ProdutoService(repo)

@app.get("/", tags=["healthcheck"])
def read_root():
    return {"message": "API de Produtos está funcionando!"}


@app.get("/produtos/{produto_id}", response_model=ProdutoRead, tags=["produtos"])
def obter_produto(produto_id: int):
    produto = produto_service.obter_produto(produto_id)

    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return ProdutoRead(id=produto.id, nome=produto.nome, preco=produto.preco, ativo=produto.ativo)


@app.get("/produtos/sku/{produto_sku}", response_model=ProdutoRead, tags=["produtos"])
def obter_produto_por_sku(produto_sku: str):
    produto = produto_service.obter_produto_por_sku(produto_sku)

    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return ProdutoRead(id=produto.id, nome=produto.nome, preco=produto.preco, ativo=produto.ativo)


@app.get("/produtos", response_model=List[ProdutoRead], tags=["produtos"])
def listar_produtos():
    produtos = produto_service.listar_produto()
    return [ProdutoRead(id=p.id, nome=p.nome, preco=p.preco, ativo=p.ativo) for p in produtos]


@app.post("/produtos", response_model=ProdutoRead, status_code=status.HTTP_201_CREATED, tags=["produtos"])
def criar_produto(produto: ProdutoCreate):
    novo_produto = produto_service.criar_produto(produto.nome, produto.preco, produto.sku, produto.data_criacao, produto.ativo)
    return ProdutoRead(id=novo_produto.id, nome=novo_produto.nome, preco=novo_produto.preco, ativo=novo_produto.ativo)

