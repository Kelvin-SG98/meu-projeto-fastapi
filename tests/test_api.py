import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "Bem-vindo à API de Recomendação de Produtos"
    }


def test_criar_produtos():
    response = client.post(
        "/produtos/",
        json={
            "nome": "Produto A",
            "categoria": "Categoria 1",
            "tags": ["tag1", "tag2"],
        },
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "Produto A"


def test_listar_produtos():
    response = client.get("/produtos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1  # Verifica se há pelo menos um produto cadastrado


def test_criar_usuario():
    response = client.post("/usuarios/", params={"nome": "Usuario Teste"})
    assert response.status_code == 200
    assert response.json()["nome"] == "Usuario Teste"
    assert response.json()["id"] == 1  # Verifica se o ID do usuário é 1


def test_listar_usuario():
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1  # Verifica se há pelo menos um usuário cadastrado


def test_criar_historico():
    response = client.post(
        "/historico_compras/1",
        json={"produtos_ids": [1]},  # Envia uma lista de IDs de produtos
    )
    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "Histórico de compras atualizado"
    }  # Verifica se a mensagem de sucesso foi retornada

def test_criar_historico_usuario_inexistente():
    response = client.post(
        "/historico_compras/999", # ID de usuário que não existe
        json={"produtos_ids": [1]},  # Envia uma lista de IDs de produtos
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Usuário não encontrado"
    }

def test_recomendar_produtos():
    response = client.post(
        "/recomendacoes/1",
        json={
            "usuario_id": 1,
            "categorias": ["Categoria 1"],
            "tags": ["tag1"],
        },
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 1  # Verifica se há pelo menos uma recomendação

def test_recomendar_produtos_historico_inexistente():
    response = client.post(
        "/recomendacoes/999",
        json={
            "usuario_id": 1,
            "categorias": ["Categoria 1"],
            "tags": ["tag1"],
        },
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Histórico de compras não encontrado"
    }