import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
WIDTH, HEIGHT = 600, 200
GROUND_HEIGHT = 20
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuração da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Run")

# Carregar imagens
dino_img = pygame.image.load("dino.png")
cactus_img = pygame.image.load("cactus.png")

# Redimensionar imagens
dino_img = pygame.transform.scale(dino_img, (50, 50))
cactus_img = pygame.transform.scale(cactus_img, (50, 50))

# Configurações do jogador
player_pos = [50, HEIGHT - GROUND_HEIGHT - 50]
player_speed = 5
jumping = False
jump_count = 10

# Configurações do cacto
cactus_pos = [WIDTH + random.randint(50, 200), HEIGHT - GROUND_HEIGHT - 50]
cactus_speed = 5

clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True

    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_pos[1] -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Movimento do cacto
    cactus_pos[0] -= cactus_speed
    if cactus_pos[0] < 0:
        cactus_pos[0] = WIDTH + random.randint(50, 200)

    # Desenhar na tela
    screen.fill(WHITE)
    screen.blit(dino_img, player_pos)
    screen.blit(cactus_img, cactus_pos)

    # Atualizar a tela
    pygame.display.flip()

    # Controle de FPS
    clock.tick(FPS)
