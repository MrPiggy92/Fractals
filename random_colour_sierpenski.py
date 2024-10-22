import turtle
import random
import time
def triangle(sidelength):
    for x in range(3):
        bob.forward(sidelength)
        bob.left(120)

def fractal(sidelength,levelofrecursion):
    if levelofrecursion == 0:
        if random.randint(0,3) == 1:
            bob.color("green")
        else:
            if random.randint(0,1) == 0:
                bob.color("red")
            else:
                bob.color("blue")
        triangle(sidelength)
    else:
        for x in range(3):
            if random.randint(0,3) == 1:
                bob.color("green")
            else:
                if random.randint(0,1) == 0:
                    bob.color("red")
                else:
                    bob.color("blue")
            fractal(sidelength/2,levelofrecursion-1)
            bob.forward(sidelength)
            bob.left(120)
sidelength = int(input("How long will the large side be?"))
levelofrecursion = int(input("How many different triangle sizes will there be?"))
start = time.time()
screen = turtle.Screen()
screen.bgcolor("black")
bob = turtle.Turtle()
bob.speed(0)
bob.color("red")
bob.hideturtle()
fractal(sidelength,levelofrecursion)
end = time.time()
print("This progam took", end-start, "seconds to run")