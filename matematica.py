def adicao(numA, numB):
    return numA + numB
def subtracao(numA, numB):
    return numA - numB
def multiplicacao(numA, numB):
    return numA * numB
def divisao(numA, numB):
    return numA / numB

print("Escolha a opção: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    numeroA = float(input("Digite o primeiro número: "))
    numeroB = float(input("Digite o segundo número: "))
    resultado = adicao(numeroA,numeroB)
elif opcao == 2:
    numeroA = float(input("Digite o primeiro número: "))
    numeroB = float(input("Digite o segundo número: "))
    resultado = subtracao(numeroA,numeroB)
elif opcao == 3:
    numeroA = float(input("Digite o primeiro número: "))
    numeroB = float(input("Digite o segundo número: "))
    resultado = multiplicacao(numeroA,numeroB)
else:
    numeroA = float(input("Digite o primeiro número: "))
    numeroB = float(input("Digite o segundo número: "))
    resultado = divisao(numeroA,numeroB)
print(f"O resultado é: {resultado:.2f}")