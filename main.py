from app.auth import hash_password, verify_password

try:
    hashed = hash_password("senha123")
    print("Senha segura:", hashed)
except Exception:
    print("Erro interno. Tente novamente mais tarde.")
