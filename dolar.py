print("Sistema de Conversão do Dólar")
print("Desenvolvido por: Karina Laurindo")
print("Copywrite 2024")
print("versão 1.0")

while True:
    valorEmDolar = float(input("Valor do produto em Dólar: US$ "))
    cotacaoDolarHoje = float(input("Digite a cotação do Dólar: R$ "))
    valorConvertido = valorEmDolar * cotacaoDolarHoje
    print(f"O valor convertido de US$ {valorEmDolar} é: R$ {valorConvertido}")
    sair = input("Deseja converter outro valor? <S/N>")
    if sair.upper() == "N":
        break
print("Agradeço pela visita. Volte sempre!")