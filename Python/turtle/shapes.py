import turtle

zelva = turtle.Turtle("turtle")
window = turtle.setup(800, 800)
window = turtle.bgcolor(45/255, 237/255, 164/255)

instructions = []

choice = input("Enter square to draw a square, ractangle to draw a ractangle, hexagon to draw a hexagon: ")

def shape(shape):
    file = open(f"Python/data/{shape}.trtl", "r")
    reading = file.read().split("\n")
    for i in reading:
        instructions.append(i) 

if choice == "square":
    shape("square")
elif choice == "ractangle":
    shape("ractangle")
elif choice == "hexagon":
    shape("hexagon")

for i in instructions:
    distance = int((i[1:]))
    direction = i[:1]
    if direction == "W":
        zelva.forward(distance)
    elif direction == "L":
        zelva.left(distance)
    elif direction == "R":
        zelva.right(distance)

turtle.done()