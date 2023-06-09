from turtle import *

title("Flower")
speed(-10)
bgcolor("black")
r, g, b = 255, 0, 0

for i in range(250):
    colormode(255)
    if i < 255 // 3:
        g += 3
    elif i < 255 * 2 // 3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255 * 4 // 3:
        g -= 3
    elif i < 255 * 5 // 3:
        r += 3
    else:
        b -= 3
    circle(280 - i, 90)
    lt(90)
    circle(280 - i, 90)
    left(18)
    pencolor(r, g, b)

hideturtle()

# Add your name here
penup()
goto(150, -300)
pencolor("white")
write("By aby", align="center", font=("Pacifico", 30, "bold"))

done()
