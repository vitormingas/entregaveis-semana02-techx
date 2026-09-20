"""
Desafio 2 - Menu de Operações Matemáticas
"""

print("===== Menu de Operações =====")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao_escolhida = int(input("Escolha uma operação (1 a 4): "))

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

match opcao_escolhida:
    case 1:
        resultado = primeiro_numero + segundo_numero
        print(f"Resultado da soma: {resultado:.2f}")
    case 2:
        resultado = primeiro_numero - segundo_numero
        print(f"Resultado da subtração: {resultado:.2f}")
    case 3:
        resultado = primeiro_numero * segundo_numero
        print(f"Resultado da multiplicação: {resultado:.2f}")
    case 4:
        if segundo_numero == 0:
            print("Erro: não é possível dividir por zero.")
        else:
            resultado = primeiro_numero / segundo_numero
            print(f"Resultado da divisão: {resultado:.2f}")
    case _:
        print("Opção inválida. Escolha um número entre 1 e 4.")
