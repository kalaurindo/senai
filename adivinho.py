import random
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando entre 1 e 20")
numero = random.randint(1,20)
while True:
    palpite = int(input("Qual o seu palpite?"))
    if palpite > numero:
        print("Você está acima!")
    elif palpite < numero:
        print("Você está abaixo!")
    else:
        print("Acertou!!!!")
        break