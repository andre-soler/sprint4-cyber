import re

def sanitize_input(text):
    return re.sub(r'[<>"]', '', text)

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)