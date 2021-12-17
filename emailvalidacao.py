"""
Função de verificação e validaçã de email.
"""

email = "Saulo@e.com"
match email:
    case email if  "@" not in email or "@." in email:
        print('Email invalido')
    case email if '.com.br' in email  or '.com' in email:
        print("Email valido")
    case _:
        print("Verifique seu email")
