import pygame
import sys

# (O código de inicialização e variáveis globais permanecem o mesmo)
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_SIZE = 10
PADDLE_SPEED = 10
BALL_SPEED = 3
START = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

score_b = 0
score_a = 0

font_file = 'Press_Start_2P/PressStart2P-Regular.ttf'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# pygame.rect(x,y,width,height)
paddle_a = pygame.Rect(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(SCREEN_WIDTH - 20 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH,
                       PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED


# Funções de estado
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                    sys.exit()

        # Renderização do menu principal

        screen.fill(BLACK)
        # Desenhe o título e as instruções aqui
        pygame.display.flip()

def game_loop():
    global ball_dx, ball_dy

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # (O código de atualização de posição das raquetes, posição da bola e detecção de colisão permanece o mesmo)

        # Verifica se a bola saiu da tela e muda para o estado de fim de jogo

        # (O código de renderização dos elementos do jogo permanece o mesmo)

def end_game(winner):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Renderização da tela de fim de jogo
        screen.fill(BLACK)
        # Desenhe o texto de vitória e instruções aqui
        pygame.display.flip()

def reset_game():
    global paddle_a, paddle_b, ball, ball_dx, ball_dy, score_a, score_b



# Inicie a FSM no estado do menu principal
main_menu()