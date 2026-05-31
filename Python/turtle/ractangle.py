import turtle
import time


zelva = turtle.Turtle("turtle")
zelva.speed(1)
window = turtle.setup(800, 800)
window = turtle.bgcolor(252/255, 3/255, 207/255)

zelva.penup()
zelva.forward(50)
zelva.right(90)
zelva.forward(25)
zelva.left(180)
zelva.pendown()

for i in range(2):
    zelva.forward(50)
    zelva.left(90)
    time.sleep(0.5)
    zelva.forward(100)
    zelva.left(90)
    time.sleep(0.5)


turtle.done()