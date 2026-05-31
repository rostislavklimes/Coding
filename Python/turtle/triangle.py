import turtle

zelva = turtle.Turtle("turtle")
zelva.speed(1)
window = turtle.setup(800, 800)
window = turtle.bgcolor(252/255, 115/255, 3/255)

zelva.penup()
zelva.forward(50)
zelva.pendown()

zelva.speed(2)

for i in range(3):
    zelva.left(120)
    zelva.forward(100)


turtle.done()