# 🔐 SecureApp – Projeto de Segurança em Python

Este projeto implementa práticas de SSDLC (Secure Software Development Life Cycle) com foco em segurança nas funcionalidades de Login e Cadastro, integradas ao pipeline de CI/CD.

## 🧱 Estrutura

- `app/`: Código principal (autenticação, sanitização)
- `tests/`: Testes automatizados com Pytest
- `.github/workflows/`: Pipeline CI/CD com GitHub Actions

## 🚀 Funcionalidades

- Validação e sanitização de entradas
- Autenticação segura com hash de senha (bcrypt)
- Tratamento de erros para evitar exposição de informações
- Testes automatizados como pré-requisitos de build
- Bloqueio de commits inseguros com pre-commit

## 🧪 Como rodar os testes

```bash
pytest
