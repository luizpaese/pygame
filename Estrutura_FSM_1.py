import pygame
import sys
import pingpong

#(Variáveis globais, inicialização)
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

#Funções de estado
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                    sys.exit()

            #Renderização menu

            screen.fill(BLACK)

            #Desenha o titulo e as instruções

        pygame.display.flip()


def game_loop():
    print("AAAAAAA")
    pingpong.game()


if __name__ == "__main__":
    main_menu()