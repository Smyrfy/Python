import pygame
pygame.init()

W, H = 800, 500
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Shapes by buttons")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
gray = (180, 180, 180)

font = pygame.font.SysFont("arial", 20)
clock = pygame.time.Clock()

# Center definitions
CENTER_X = W // 2
CENTER_Y = H // 2
SHAPE_SIZE = 150

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
        rect_width, rect_height = SHAPE_SIZE, SHAPE_SIZE * 0.7
        rect_x = CENTER_X - rect_width // 2
        rect_y = CENTER_Y - rect_height // 2
        pygame.draw.rect(sc, blue, (rect_x, rect_y, rect_width, rect_height), 3)

    elif shape_id == 2:
        line_length = SHAPE_SIZE + 50
        start_pos = (CENTER_X - line_length // 2, CENTER_Y - 50)
        end_pos = (CENTER_X + line_length // 2, CENTER_Y + 50)
        pygame.draw.line(sc, green, start_pos, end_pos, 5)

    elif shape_id == 3:
        radius = SHAPE_SIZE // 3
        pygame.draw.circle(sc, red, (CENTER_X, CENTER_Y), radius, 3)

    elif shape_id == 4:
        ellipse_width, ellipse_height = SHAPE_SIZE, SHAPE_SIZE // 2
        ellipse_x = CENTER_X - ellipse_width // 2
        ellipse_y = CENTER_Y - ellipse_height // 2
        pygame.draw.ellipse(sc, yellow, (ellipse_x, ellipse_y, ellipse_width, ellipse_height), 3)

    elif shape_id == 5:

        polygon_points_relative = [
            (0, -SHAPE_SIZE // 3),
            (SHAPE_SIZE // 4, 0),
            (SHAPE_SIZE // 6, SHAPE_SIZE // 3),
            (-SHAPE_SIZE // 6, SHAPE_SIZE // 3),
            (-SHAPE_SIZE // 4, 0)
        ]

        final_points = [
            (px + CENTER_X, py + CENTER_Y)
            for px, py in polygon_points_relative
        ]

        pygame.draw.polygon(sc, blue, final_points, 3)


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


    pygame.display.update()
    clock.tick(60)

pygame.quit()
