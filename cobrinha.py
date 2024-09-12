import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 1000
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (213, 50, 80)

# Configurações da cobrinha
tamanho_bloco = 20
velocidade = 15

# Fonte
font_style = pygame.font.SysFont(None, 50)

def mensagem(msg, cor):
    texto = font_style.render(msg, True, cor)
    tela.blit(texto, [largura_tela / 6, altura_tela / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = largura_tela / 2
    y1 = altura_tela / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
    foody = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0

    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            tela.fill(preto)
            mensagem("Você perdeu! Pressione Q para sair ou C para jogar novamente", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -tamanho_bloco
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = tamanho_bloco
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -tamanho_bloco
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = tamanho_bloco
                    x1_change = 0

        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        tela.fill(preto)
        pygame.draw.rect(tela, verde, [foodx, foody, tamanho_bloco, tamanho_bloco])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(tela, branco, [segment[0], segment[1], tamanho_bloco, tamanho_bloco])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, largura_tela - tamanho_bloco) / 20.0) * 20.0
            foody = round(random.randrange(0, altura_tela - tamanho_bloco) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

gameLoop()
