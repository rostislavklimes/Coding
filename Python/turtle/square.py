import turtle
import time


zelva = turtle.Turtle("turtle")
zelva.speed(1)
window = turtle.setup(800, 800)
window = turtle.bgcolor(244/255, 255/255, 28/255)

zelva.penup()
zelva.forward(50)
zelva.left(90)
zelva.pendown()
zelva.forward(50)
time.sleep(0.5)
for i in range(4):
    zelva.left(90)
    zelva.forward(100)
    time.sleep(0.5)


turtle.done()