import jwt
import datetime
import pytest
from main import app, SECRET_KEY, USERS


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def make_token(username, role=None, exp_minutes=5):
    user = USERS[username]
    payload = {
        "sub": username,
        "role": role if role is not None else user["role"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=exp_minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def test_login_success_admin(client):
    response = client.post("/login", json={
        "username": "julian.lara",
        "password": "123456"
    })

    assert response.status_code == 200
    data = response.get_json()
    assert "token" in data


def test_login_invalid_credentials(client):
    response = client.post("/login", json={
        "username": "julian.lara",
        "password": "wrong-password"
    })

    assert response.status_code == 401
    assert response.get_json()["message"] == "Credenciales inválidas"


def test_profile_without_token_returns_401(client):
    response = client.get("/profile")

    assert response.status_code == 401
    assert response.get_json()["message"] == "Token requerido"


def test_profile_with_valid_token_returns_200(client):
    token = make_token("julian.lara")
    response = client.get("/profile", headers={
        "Authorization": f"Bearer {token}"
    })

    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Acceso concedido"
    assert data["user"]["role"] == "admin"


def test_profile_with_invalid_token_returns_401(client):
    response = client.get("/profile", headers={
        "Authorization": "Bearer token-invalido"
    })

    assert response.status_code == 401
    assert response.get_json()["message"] == "Token inválido"


def test_profile_with_expired_token_returns_401(client):
    token = make_token("julian.lara", exp_minutes=-1)
    response = client.get("/profile", headers={
        "Authorization": f"Bearer {token}"
    })

    assert response.status_code == 401
    assert response.get_json()["message"] == "Token expirado"


def test_admin_zone_with_admin_token_returns_200(client):
    token = make_token("julian.lara")
    response = client.get("/admin-zone", headers={
        "Authorization": f"Bearer {token}"
    })

    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Acceso concedido al área admin"
    assert data["user"]["role"] == "admin"


def test_admin_zone_with_user_token_returns_403(client):
    token = make_token("jose.torres")
    response = client.get("/admin-zone", headers={
        "Authorization": f"Bearer {token}"
    })

    assert response.status_code == 403
    assert response.get_json()["message"] == "No tienes permiso"


def test_admin_zone_without_token_returns_401(client):
    response = client.get("/admin-zone")

    assert response.status_code == 401
    assert response.get_json()["message"] == "Token requerido"


def test_admin_zone_with_manipulated_token_returns_401(client):
    token = make_token("julian.lara")
    manipulated_token = token[:-1] + ("a" if token[-1] != "a" else "b")

    response = client.get("/admin-zone", headers={
        "Authorization": f"Bearer {manipulated_token}"
    })

    assert response.status_code == 401
    assert response.get_json()["message"] == "Token inválido"