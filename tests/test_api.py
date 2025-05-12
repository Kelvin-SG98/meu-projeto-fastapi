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
