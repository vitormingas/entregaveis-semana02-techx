"""
Desafio 3 - Análise de Números
"""

quantidade_numeros = 5
soma_numeros = 0
maior_numero = None
menor_numero = None

for posicao in range(1, quantidade_numeros + 1):
    numero_digitado = float(input(f"Digite o {posicao}º número: "))

    soma_numeros += numero_digitado

    if maior_numero is None or numero_digitado > maior_numero:
        maior_numero = numero_digitado

    if menor_numero is None or numero_digitado < menor_numero:
        menor_numero = numero_digitado

media_numeros = soma_numeros / quantidade_numeros

print(f"Soma: {soma_numeros:.2f}")
print(f"Média: {media_numeros:.2f}")
print(f"Maior valor: {maior_numero:.2f}")
print(f"Menor valor: {menor_numero:.2f}")
