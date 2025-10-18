from app.auth import hash_password, verify_password

def test_password_hashing():
    senha = "segura123"
    hashed = hash_password(senha)
    assert verify_password(senha, hashed)
