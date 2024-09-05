print("Sistema de Cálculo de Juros") 
print("Desenvolvido por: Karina Laurindo")
print("Copywrite 2024")
print("versão 1.0")

while True:
    valorDaConta = float(input("Digite o valor da Conta: R$ "))
    diasAtraso = int(input("Digite os dias de atraso: "))
    jurosPorDia = float(input("Digite o valor dos juros: "))
    valorCorrigido = valorDaConta + (valorDaConta * diasAtraso * (jurosPorDia/100))
    print(f"O valor corrigido é: R$ {valorCorrigido:.2f}")
    sair = input("Deseja calcular outro valor? <S/N>")
    if sair.upper() == "N":
        break
print("Agradeço pela visita. Volte sempre!")