from __future__ import annotations  
from typing import List
from fastapi import FastAPI, HTTPException, status

try:
    from src.models.produto_schemas import ProdutoCreate, ProdutoRead, ProdutoUpdate
    from src.services.produto_repo_memory import ProdutoRepositoryMemory
    from src.services.produto_service import ProdutoService
except ModuleNotFoundError:
    # Suporta execução direta: `python src/main.py`.
    from models.produto_schemas import ProdutoCreate, ProdutoRead, ProdutoUpdate
    from services.produto_repo_memory import ProdutoRepositoryMemory
    from services.produto_service import ProdutoService


app = FastAPI(
    title="API de Produtos",
    description="Uma API para gerenciar produtos usando FastAPI e um repositório em memória.",
    version="1.0.0"
)

repo = ProdutoRepositoryMemory()
produto_service = ProdutoService(repo)

# Rota de healthcheck
@app.get("/", tags=["healthcheck"])
def read_root():
    return {"message": "API de Produtos está funcionando!"}

# Pesquisar produto por ID
@app.get("/produtos/{produto_id}", response_model=ProdutoRead, status_code=status.HTTP_200_OK, tags=["produtos"])
def obter_produto(produto_id: int):
    produto = produto_service.obter_produto(produto_id)

    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return ProdutoRead(id=produto.id, nome=produto.nome, sku=produto.sku, data_criacao=produto.data_criacao, preco=produto.preco, ativo=produto.ativo)

# Pesquisar produto por SKU
@app.get("/produtos/sku/{produto_sku}", response_model=ProdutoRead, status_code=status.HTTP_200_OK, tags=["produtos"])
def obter_produto_por_sku(produto_sku: str):
    produto = produto_service.obter_produto_por_sku(produto_sku)

    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return ProdutoRead(id=produto.id, nome=produto.nome, sku=produto.sku, data_criacao=produto.data_criacao, preco=produto.preco, ativo=produto.ativo)

# Listar todos os produtos
@app.get("/produtos", response_model=List[ProdutoRead], status_code=status.HTTP_200_OK, tags=["produtos"])
def listar_produtos():
    produtos = produto_service.listar_produto()

    if not produtos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não há produtos cadastrados")
    return [ProdutoRead(id=p.id, nome=p.nome, sku=p.sku, data_criacao=p.data_criacao, preco=p.preco, ativo=p.ativo) for p in produtos]

# Criar um novo produto
@app.post("/produtos", status_code=status.HTTP_201_CREATED, tags=["produtos"])
def criar_produto(produto: ProdutoCreate):
    novo_produto = produto_service.criar_produto(produto.nome, produto.preco, produto.sku, produto.data_criacao, produto.ativo)
    return ProdutoRead(id=novo_produto.id, nome=novo_produto.nome, sku=novo_produto.sku, data_criacao=novo_produto.data_criacao, preco=novo_produto.preco, ativo=novo_produto.ativo)

# Atualizar um produto existente
@app.put("/produtos/{produto_id}", response_model=ProdutoRead, status_code=status.HTTP_200_OK, tags=["produtos"])
def atualizar_produto(produto_id: int, produto: ProdutoUpdate):
    produto_existente = produto_service.obter_produto(produto_id)

    if not produto_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    
    nome: str = produto.nome if produto.nome is not None else produto_existente.nome
    preco: float = produto.preco if produto.preco is not None else produto_existente.preco
    sku: str = produto.sku if produto.sku is not None else produto_existente.sku 

    produto_atualizado = produto_service.atualizar_produto(
        id_ = produto_id,
        nome = nome, 
        preco = preco, 
        sku = sku, 
        ativo = produto.ativo)
    
    if not produto_atualizado:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao atualizar o produto") 
    
    return ProdutoRead(id=produto_atualizado.id, nome=produto_atualizado.nome, sku=produto_atualizado.sku, data_criacao=produto_atualizado.data_criacao, preco=produto_atualizado.preco, ativo=produto_atualizado.ativo)

# Remover um produto
@app.delete("/produtos/{produto_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["produtos"])
def remover_produto(produto_id: int):
    produto_existente = produto_service.obter_produto(produto_id)

    if not produto_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    
    sucesso = produto_service.remover_produto(produto_id)

    if not sucesso:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao remover o produto")      
    
