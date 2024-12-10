#Abdullah Hassan
#P4LAB1
#11/12/24
#CTI 110

import turtle
t = turtle.Turtle()
#background
win = turtle.Screen()
win.bgcolor("black")

#display options
t.pensize(4)
t.pencolor("green")
t.shape("turtle")

#triangle
for side in range(3):
    t.forward(100)
    t.right(120)
    
t.pencolor("purple")
#trippy triangle
t.fillcolor("deeppink4")
t.begin_fill()
for side in range(30):
    t.forward(100)
    t.right(130)
t.end_fill()

#square
t.forward(105)
t.pencolor("limegreen")
for side in range(4):
    t.forward(100)
    t.left(90)

#pentagon/shuriken/windmill
t.pencolor("khaki")
for side in range(4):
    t.backward(95)
    t.forward(145)
    t.left(80)
    #t.forward(150)
    #t.left(100)

#rectangle
t.forward(200)
t.pencolor("tomato")
for side in range(4):
    t.backward(95)
    t.forward(145)
    t.left(80)
    t.forward(150)
    t.left(100)


#snowflake
t.forward(199)
t.pencolor("white")
for flake in range (8):
    t.forward(120)
    t.backward(120)
    t.left(45)
