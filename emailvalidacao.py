"""
Função de verificação e validação de email.
Função python 3.10
"""

email = "Saulo@e.com"
match email:
    case email if  "@" not in email or "@." in email:
        print('Email invalido')
    case email if '.com.br' in email  or '.com' in email:
        print("Email valido")
    case _:
        print("Verifique seu email")
