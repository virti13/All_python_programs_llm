import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(100):
    t.forward(i * 5)
    t.right(144)

turtle.done()