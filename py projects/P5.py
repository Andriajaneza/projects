import turtle

t = turtle.Turtle()
t.speed(9999999)
t.color("red")

for i in range(32):
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.left(10)

t.color("aqua")

for i in range(32):
    for i in range(4):
        t.forward(150)
        t.left(90)
    t.left(10)

t.color("green")

t.begin_fill()
for i in range(36):
    for i in range(4):
        t.forward(60)
        t.left(90)
    t.left(10)
t.end_fill()

turtle.exitonclick()
