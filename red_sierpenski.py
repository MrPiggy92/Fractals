import turtle
import time
import math
def triangle(sidelength):
    for x in range(3):
        bob.forward(sidelength)
        bob.left(120)

def fractal(sidelength,levelofrecursion):
    if levelofrecursion == 0:
        triangle(sidelength)
    else:
        for x in range(3):
            fractal(sidelength/2,levelofrecursion-1)
            bob.forward(sidelength)
            bob.left(120)
def centre_the_triangle(sidelength):
    centered_x = 0-(sidelength/2)
    centered_y = 0-(((math.sqrt(3)/2)*sidelength)/2)
    bob.goto(centered_x,centered_y)
sidelength = int(input("How long will the large side be?"))
levelofrecursion = int(input("How many different triangle sizes will there be?"))
start = time.time()
WIDTH = HEIGHT = sidelength + 20
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
bob = turtle.Turtle()
bob.speed(0)
bob.color("red")
bob.hideturtle()
bob.penup()
centre_the_triangle(sidelength)
bob.pendown()
fractal(sidelength,levelofrecursion)
end = time.time()
print("This progam took", end-start, "seconds to run")