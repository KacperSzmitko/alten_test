def test_create_user(client):
    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "StrongPass1!",
        "is_superuser": False,
    }
    response = client.post("/api/v1/users", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "hashed_password" in data


def test_get_users(client):
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
