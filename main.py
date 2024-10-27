from turtle import Turtle, Screen
from random import randint, choice


# Create the turtle object
t = Turtle()

# List of possible colors
colors = ['orange', 'red', 'green', 'blue',
          'black', 'lime', 'purple', 'cyan']


def draw_circle(t, radius, position, color):
    t.penup()  # Lift the pen to move without drawing
    t.goto(position)  # Move the turtle to the specified position
    t.pendown()  # Place the pen down to start drawing
    t.color(color[i])
    t.begin_fill()
    t.circle(radius)  # Draw a circle with the given radius
    t.end_fill()



# Draw 8 circles with random positions, radii, and colors
for i in range(10):
    position = (randint(-100, 200), randint(-200, 300))  # Random position
    radius = randint(10, 80)  # Random radius
    color = (colors)  # Random color from the list
    draw_circle(t, radius, position, color)
    
done()

# Create a screen to view the result
screen = Screen()
screen.mainloop()
