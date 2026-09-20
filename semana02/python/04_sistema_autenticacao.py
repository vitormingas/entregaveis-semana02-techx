"""
Desafio 4 - Sistema de Autenticação
"""

senha_correta = "senha"
numero_tentativas = 0
limite_tentativas = 3
acesso_liberado = False

while numero_tentativas < limite_tentativas:
    senha_digitada = input("Digite a senha: ")
    numero_tentativas += 1

    if senha_digitada == senha_correta:
        acesso_liberado = True
        break
    else:
        tentativas_restantes = limite_tentativas - numero_tentativas
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}")

if acesso_liberado:
    print("Acesso liberado! Senha correta.")
else:
    print("Acesso bloqueado. Número máximo de tentativas excedido.")
