import pytest
from app.utils import sanitize_input, is_valid_email

def test_sanitize_input_removes_tags():
    entrada = '<script>alert("hack")</script>'
    resultado = sanitize_input(entrada)
    assert '<' not in resultado and '>' not in resultado and '"' not in resultado

def test_sanitize_input_preserves_text():
    entrada = 'Olá, mundo!'
    resultado = sanitize_input(entrada)
    assert resultado == 'Olá, mundo!'

def test_valid_email_format():
    email = 'usuario@email.com'
    assert is_valid_email(email)

def test_invalid_email_format():
    email = 'usuario@email'
    assert not is_valid_email(email)

def test_email_with_special_chars():
    email = 'user.name+123@dominio.co.uk'
    assert is_valid_email(email)
