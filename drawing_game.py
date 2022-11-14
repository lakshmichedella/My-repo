import pygame, sys

WIDTH, HEIGHT = 800, 800

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Draw')

WINDOW.fill('white')
# brush = pygame.Rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION) and pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            pygame.draw.ellipse(WINDOW, 'black', [pos[0], pos[1], 10, 10])
    pygame.display.flip()
    clock.tick(FPS)
