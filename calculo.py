rodar = "S"
#while rodar == "S" or "s" :
while rodar.upper() == "S" :
    operacao = input("Digite 1 para adição; 2 para subtração; 3 para multiplicação; 4 para divisão: ")
    if not operacao.isdigit():
        continue
    if int(operacao) > 4 or int(operacao) < 1:
        continue
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite outro número: "))
    if operacao == "1":
        resultado = numero1 + numero2
    elif operacao == "2":
        resultado = numero1 - numero2
    elif operacao == "3":
        resultado = numero1 * numero2
    else:
        resultado = numero1 / numero2
    print("O resultado é:", resultado)
    rodar = input("Deseja fazer outra operação? <S/N>")
    while rodar.upper() != "S" and rodar.upper() != "N":
        rodar = input("Opção inválida. Digite S ou N: ")