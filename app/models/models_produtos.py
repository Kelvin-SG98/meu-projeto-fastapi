from pydantic import BaseModel
from typing import Dict, List, Optional  # Adicione Optional


# Modelo base para produto
class ProdutoBase(BaseModel):
    nome: str
    categoria: str
    tags: List[str]


# Modelo para criar um produto
class CriarProduto(ProdutoBase):
    pass

# Modelo de produto com ID
class Produto(ProdutoBase):
    id: int


# Modelo para histórico de compras do usuário
class HistoricoCompras(BaseModel):
    produtos_ids: List[int]


# Modelo para preferências do usuário
class Preferencias(BaseModel):
    # categorias: List[str] | None = None
    categorias: Optional[List[str]] = None  # Substitua | por Optional
    # tags: List[str] | None = None
    tags: Optional[List[str]] = None  # Substitua | por Optional