import pytest

from application import app, db


@pytest.fixture
def client(tmp_path):
    app.config["TESTING"]=True
    app.config["SQLALCHEMY_DATABASE_URI"]=(
        f"sqlite:///{tmp_path/'test.db'}"
    )
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


def test_home(client):
    response=client.get("/")

    assert response.status_code==200

def test_get_drinks(client):
    response=client.get("/drinks")
    assert response.status_code==200
    assert response.is_json

def test_add_drink(client):
    response=client.post(
        "/drinks",
        json={
            "name": "Test Coffee",
            "description": "Coffee created by pytest"
        }
    )

    assert response.status_code==201
    assert response.is_json
    assert "id" in response.json

def test_get_drink_by_id(client):
    create_response=client.post(
        "/drinks",
        json={
            "name": "Latte Test",
            "description": "Test latte"
        }
    )
    drink_id=create_response.json["id"]
    response=client.get(f"/drinks/{drink_id}")

    assert response.status_code==200
    assert response.json["name"]=="Latte Test"
    assert response.json["description"]=="Test latte"

def test_delete_drink(client):
    create_response=client.post(
        "/drinks",
        json={
            "name":"Delete Me",
            "description":"Temporary test drink"
        }
    )
    drink_id=create_response.json["id"]
    response=client.delete(f"/drinks/{drink_id}")
    assert response.status_code==200
    assert response.json["message"]=="yeeeeeeeeet"

    get_response=client.get(f"/drinks/{drink_id}")
    assert get_response.status_code==404

def test_get_nonexistent_drink(client):
    response=client.get("/drinks/9999")

    assert response.status_code==404

def test_add_drink_without_name(client):
    response=client.post(
        "/drinks",
        json={"description":"Missing name"}
    )
    assert response.status_code==400

def test_add_drink_with_blank_name(client):
    response=client.post(
        "/drinks",
        json={"name":"   "}
    )
    assert response.status_code==400

def test_add_duplicate_drink(client):
    payload={
        "name":"Test Coffee",
        "description":"First Entry"
    }
    first_response=client.post("/drinks", json=payload)
    second_response=client.post("/drinks", json=payload)

    assert first_response.status_code==201
    assert second_response.status_code==409

def test_add_drink_with_invalid_json(client):
    response=client.post(
        "/drinks",
        data="not valid json",
        content_type="application/json"
    )
    assert response.status_code==400