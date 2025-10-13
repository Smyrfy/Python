import pygame
pygame.init()

W = 600
H = 400
sc = pygame.display.set_mode((W, H))

pygame.display.set_caption ("Mouse Event")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:FPS = 60

        clock = pygame.time.Clock()
        while 1:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   exit()

               elif event.type == pygame.MOUSEBUTTONDOWN:
                   print("Нажата кнопка: ", event.button)
               elif event.type == pygame.MOUSEMOTION:
                   print("Позиция мыши: ", event.pos)
           clock.tick(FPS)
