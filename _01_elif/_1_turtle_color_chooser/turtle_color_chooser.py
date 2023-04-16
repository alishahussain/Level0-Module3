import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    bob = turtle.Turtle()
    bob.pendown()
    bob.circle(100)
    #      3) Set the pen width to 10
    bob.pensize(10)
    #      4) Ask the user what color pen they would like to draw with
    for i in  range(10):
        question = simpledialog.askstring(title='none',prompt='what color pen do u like to draw with?')
        #      5) Use an if/else statement to set the pen color that the user
        #         requested
        if question== question:
            bob.color(question)
            bob.circle(100)
        #      6) If the user doesn't enter anything, choose a random color
        if question=='':
            bob.color(get_random_color())
            bob.circle(100)
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
