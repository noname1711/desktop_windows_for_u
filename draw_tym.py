import turtle as t
import pygame
from threading import Thread

# Hàm để phát nhạc
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("cute.mp3")
    pygame.mixer.music.play(-1)  # -1 để phát nhạc lặp lại liên tục

# Chạy phát nhạc song song với vẽ bằng cách sử dụng Thread
music_thread = Thread(target=play_music)
music_thread.start()

# Bắt đầu vẽ với Turtle
em = t.Turtle()
s = t.Screen()
s.title("Give U My Heart :3")  # Đặt tiêu đề mới cho cửa sổ Turtle
s.bgcolor("white")

t.pensize(2)

def rectangle(hor, ver, col):
    em.pendown()  # tao con tro
    em.pensize(1)
    em.color(col)
    em.begin_fill()
    for counter in range(1, 3):
        em.forward(hor)
        em.right(90)
        em.forward(ver)
        em.right(90)
    em.end_fill()
    em.penup()

em.speed(3)
em.color("red", "pink")

em.penup()
em.goto(-140, -75)
em.pendown()
rectangle(15, 140, 'magenta')
em.goto(-60, -75)
rectangle(15, 125, "magenta")
em.goto(-60, -200)
rectangle(100, 15, 'magenta')
em.goto(100, -200)
rectangle(15, -125, 'magenta')
rectangle(100, 15, 'magenta')
em.goto(185, -75)
rectangle(15, 125, 'magenta')
em.end_fill()
em.hideturtle()

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.speed(3)
t.color("red", "pink")

t.begin_fill()
t.left(140)
t.forward(111.65)
curve()

t.left(120)
curve()
t.forward(111.65)

em.color("red")
em.penup()
em.goto(10, 74)
em.pendown()
em.write('tặng baby của tôi =)))', align='center', font=('Times New Roman', 24, 'bold'))

t.hideturtle()
t.mainloop()
