# Python program to print partial Koch Curve.
# importing the libraries : turtle standard
# graphics library for python
import turtle

#function to create koch snowflake or koch curve
def snowflake(lengthSide, levels):
    if levels == 0:
        bob.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels-1)
    bob.left(60)
    snowflake(lengthSide, levels-1)
    bob.right(120)
    snowflake(lengthSide, levels-1)
    bob.left(60)
    snowflake(lengthSide, levels-1)

# main function
if __name__ == "__main__":
    bob = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("black")
    # defining the speed of the turtle
    bob.color("red")
    bob.hideturtle()
    bob.speed(0)
    length = 300.0
    bob.fillcolor("red")

    # Pull the pen up – no drawing when moving.
    bob.penup()
    
    # Move the turtle backward by distance,
    # opposite to the direction the turtle
    # is headed.
    # Do not change the turtle’s heading.
    bob.backward(length/2.0)

    # Pull the pen down – drawing when moving.
    bob.pendown()
    
    bob.begin_fill()
    for x in range(3):
        snowflake(length, 4)
        bob.right(120)
    bob.end_fill()
    # To control the closing windows of the turtle
    turtle.mainloop()
