from turtle import Turtle, Screen


def star(t, width, size, color):
    t.color(color)
    t.width(width)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


# Create the turtle object
t = Turtle()

# Call the star function with the correct parameters
star(t, 2, 100, 'purple')

# Create a screen to view the result
screen = Screen()
screen.mainloop()
