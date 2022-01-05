from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_all_users():
    response = client.get("/users")
    assert response.status_code == 200


# def test_create_user():
#     response = client.post("/users")
#     assert response.status_code == 201
#
