import pygame
import sys

pygame.init()



SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255,255,255)
BLACK = (0,0,0)
font_file = '../font/PressStart2P-Regular.ttf'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        screen.fill(BLACK)
        title_font = pygame.font.Font(font_file, 36)
        title_text = title_font.render("Luiz Pong", True, WHITE)
        title_rect = title_text.get_rect(center =(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(title_text, title_rect)


    pygame.display.flip()