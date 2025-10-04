from tkinter import *

# настройки окна
WIDTH = 900
HEIGHT = 300

# настройки ракетки
PAD_W = 10
PAD_H = 100

# настройки мяча
BALL_RADIUS = 30
BALL_X_CHANGE = 10
BALL_Y_CHANGE = 6

# окно
root = Tk()
root.title("Пинг-понг")

# canvas
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#483D8B")
c.pack()

# элементы игрового поля
c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="white")
BALL = c.create_oval(WIDTH/2 - BALL_RADIUS/2,
                     HEIGHT/2 - BALL_RADIUS/2,
                     WIDTH/2 + BALL_RADIUS/2,
                     HEIGHT/2 + BALL_RADIUS/2, fill="#FF4500")

LEFT_PAD = c.create_line(PAD_W/2, HEIGHT/2 - PAD_H/2, PAD_W/2, HEIGHT/2 + PAD_H/2,
                         width=PAD_W, fill="#48D1CC")
RIGHT_PAD = c.create_line(WIDTH - PAD_W/2, HEIGHT/2 - PAD_H/2, WIDTH - PAD_W/2, HEIGHT/2 + PAD_H/2,
                          width=PAD_W, fill="#48D1CC")

# начальные скорости
ball_x_speed = BALL_X_CHANGE
ball_y_speed = BALL_Y_CHANGE
left_pad_speed = 0
right_pad_speed = 0


def move_ball():
    global ball_x_speed, ball_y_speed

    # движение мяча
    c.move(BALL, ball_x_speed, ball_y_speed)

    ball_left, ball_top, ball_right, ball_bottom = c.coords(BALL)

    # отскок от верхней и нижней границы
    if ball_top <= 0 or ball_bottom >= HEIGHT:
        ball_y_speed = -ball_y_speed

    # координаты ракеток
    left_pad_pos = c.coords(LEFT_PAD)
    right_pad_pos = c.coords(RIGHT_PAD)

    # отскок от левой ракетки
    if ball_left <= PAD_W and left_pad_pos[1] < ball_bottom and left_pad_pos[3] > ball_top:
        ball_x_speed = abs(ball_x_speed)

    # отскок от правой ракетки
    if ball_right >= WIDTH - PAD_W and right_pad_pos[1] < ball_bottom and right_pad_pos[3] > ball_top:
        ball_x_speed = -abs(ball_x_speed)


def move_pads():
    # двигаем ракетки
    c.move(LEFT_PAD, 0, left_pad_speed)
    c.move(RIGHT_PAD, 0, right_pad_speed)

    # не даем выйти за границы
    for pad in [LEFT_PAD, RIGHT_PAD]:
        pos = c.coords(pad)
        if pos[1] < 0:
            c.move(pad, 0, -pos[1])
        elif pos[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - pos[3])


def main():
    move_ball()
    move_pads()
    root.after(30, main)


# управление
def move_pad(event):
    global left_pad_speed, right_pad_speed
    if event.keysym == 'w':
        left_pad_speed = -10
    elif event.keysym == 's':
        left_pad_speed = 10
    elif event.keysym == 'Up':
        right_pad_speed = -10
    elif event.keysym == 'Down':
        right_pad_speed = 10


def stop_pad(event):
    global left_pad_speed, right_pad_speed
    if event.keysym in ('w', 's'):
        left_pad_speed = 0
    elif event.keysym in ('Up', 'Down'):
        right_pad_speed = 0


root.bind("<KeyPress>", move_pad)
root.bind("<KeyRelease>", stop_pad)

main()
root.mainloop()
