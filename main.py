from turtle import Turtle, Screen
from random import randint, choice


# Create the turtle object
pencil = Turtle()

# List of possible colors


def draw_circle(p, radius, position, color):
    p.penup()  # Lift the pen to move without drawing
    p.goto(position)  # Move the turtle to the specified position
    p.pendown()  # Place the pen down to start drawing
    p.color(color[i])
    p.begin_fill()
    p.circle(radius)  # Draw a circle with the given radius
    p.end_fill()


colors = ['orange', 'red', 'green', 'blue',
          'black', 'lime', 'purple', 'cyan']
for i in range(10):
    position = (randint(-100, 200), randint(-200, 300))  # Random position
    radius = randint(10, 80)  # Random radius
    color = (colors)  # Random color from the list
    draw_circle(pencil, radius, position, color)


# Create a screen to view the result
screen = Screen()
screen.mainloop()


# method square

def square(p, size, color):
    p.color(color)
    p.begin_fill()
    for _ in range(4):
        p.forward(size)
        p.right(90)
        p.end_fill()

    drawSquare=Turtle.square(p,10,'yellow')

    done()