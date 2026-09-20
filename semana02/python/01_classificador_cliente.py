"""
Desafio 1 - Classificador de Cliente
"""

idade_cliente = int(input("Digite a idade do cliente: "))
renda_cliente = float(input("Digite a renda mensal do cliente: R$ "))

if renda_cliente >= 10000 and idade_cliente >= 25:
    categoria = "Diamante"
elif renda_cliente >= 5000:
    categoria = "Ouro"
elif renda_cliente >= 2000:
    categoria = "Prata"
else:
    categoria = "Bronze"

print(f"Cliente com {idade_cliente} anos e renda de R$ {renda_cliente:.2f}: {categoria}")
