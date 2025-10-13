import pygame
pygame.init()

W = 600
H = 400
sc = pygame.display.set_mode((W, H))

pygame.display.set_caption ("Mouse Event")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FPS = 60
clock = pygame.time.Clock()

sc.fill(WHITE)
pygame.display.update()
sp = None

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill(WHITE)
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_focused():
        pygame.draw.circle(sc, BLUE, pos, 7)

    pygame.display.update()

    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        if sp is None:
            sp = pygame.mouse.get_pos()
        pos = pygame.mouse.get_pos()
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]
        sc.fill(WHITE)
        pygame.draw.rect(sc, RED, (sp[0], sp[1], width, height), 2)
        pygame.display.update()
    else:
        sp = None

    clock.tick(FPS)
