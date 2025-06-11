from turtle import *

# Setup
bgcolor('white')
speed(2)
pensize(2)

def draw_parallelogram(color, pos, angle, width, height):
    penup()
    goto(pos)
    setheading(angle)
    pendown()
    fillcolor(color)
    begin_fill()
    for _ in range(2):
        forward(width)
        left(120)
        forward(height)
        left(60)
    end_fill()

# Elemen merah
draw_parallelogram('red', (-50, 100), 0, 80, 40)

# Elemen biru
draw_parallelogram('blue', (-120, -50), 0, 100, 50)

# Elemen hijau
draw_parallelogram('green', (0, -50), 0, 60, 30)

# Tulisan Pertamina
penup()
goto(-80, -150)
color('black')
write("PERTAMINA", font=("Arial Black", 30, "normal"))

hideturtle()
done()