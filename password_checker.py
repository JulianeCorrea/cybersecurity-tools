import re

def check_password_strength(password):
    # Critérios de força
    length = len(password) >= 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    score = sum([length, bool(has_upper), bool(has_lower), bool(has_digit), bool(has_special)])
    
    if score == 5:
        return "Senha muito forte! 🔒"
    elif score >= 3:
        return "Senha moderada. ✅"
    else:
        return "Senha fraca! ❌ (Use 8+ caracteres, maiúsculas, números e símbolos)"

# Teste
senha = input("Digite uma senha para verificar: ")
print(check_password_strength(senha))
