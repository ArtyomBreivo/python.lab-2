def is_password_good(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True
password = "SecureP@ss1"
result = is_password_good(password)
print(result)  # Вернет True