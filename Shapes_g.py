import pygame
pygame.init()

W, H = 800, 500
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Shapes by buttons")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
gray = (180, 180, 180)

font = pygame.font.SysFont("arial", 20)
clock = pygame.time.Clock()


buttons = [
    {"id": 1, "text": "Rectangle", "rect": pygame.Rect(20, 20, 180, 40)},
    {"id": 2, "text": "line", "rect": pygame.Rect(20, 70, 180, 40)},
    {"id": 3, "text": "Circle", "rect": pygame.Rect(20, 120, 180, 40)},
    {"id": 4, "text": "Ellipse", "rect": pygame.Rect(20, 170, 180, 40)},
    {"id": 5, "text": "Polygon", "rect": pygame.Rect(20, 220, 180, 40)},
]


current_shape = None


def draw_buttons():
    for btn in buttons:
        pygame.draw.rect(sc, gray, btn["rect"])
        pygame.draw.rect(sc, black, btn["rect"], 2)
        text = font.render(btn["text"], True, black)
        sc.blit(text, (btn["rect"].x + 10, btn["rect"].y + 10))


def draw_shape(shape_id):
    if shape_id == 1:
        pygame.draw.rect(sc, blue, (300, 100, 150, 100), 3)
    elif shape_id == 2:
        pygame.draw.line(sc, green, (300, 80), (550, 200), 5)
    elif shape_id == 3:
        pygame.draw.circle(sc, red, (450, 250), 60, 3)
    elif shape_id == 4:
        pygame.draw.ellipse(sc, yellow, (320, 300, 200, 100), 3)
    elif shape_id == 5:
        pygame.draw.polygon(sc, blue, [(350, 400), (420, 350), (500, 420), (470, 470), (370, 470)], 3)


running = True
while running:
    sc.fill(white)
    draw_buttons()


    if current_shape is not None:
        draw_shape(current_shape)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse = event.pos
            for btn in buttons:
                if btn["rect"].collidepoint(mouse):
                    current_shape = btn["id"]
                    print(f"when button click: {btn['text']}")

    pygame.display.update()
    clock.tick(60)

pygame.quit()
