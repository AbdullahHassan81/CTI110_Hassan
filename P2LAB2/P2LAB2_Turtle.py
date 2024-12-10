#CTI 110
#P2LAB2 - Turtle
#10/18

# using lists and loops to draw 

import turtle
t = turtle.Turtle()
# remember pensize, pencolor
t.pensize(3)
t.pencolor("green")

#simple loop
for length in [100, 200, 100, 200]:
    t.forward(length)
    t.right(90)

t.pencolor("black")
for length in [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]:
    t.forward(length)
    t.right(81)
    

sides = 5
length = 100
angle = 360 / sides

for color in ["red", "green", "blue", "orange", "black"]:
    t.pencolor(orange)
    t.forward(95)
    t.right(35)
