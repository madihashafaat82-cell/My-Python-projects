import turtle

# Screen setup
turtle.Screen().bgcolor("black")
turtle.title("Fun with Shapes")

# Turtle setup
b = turtle.Turtle()
b.speed(3)
b.width(2)

# for Triangle 
b.penup()
b.goto(-200, 0)
b.pendown()
b.color("white", "Purple")
b.begin_fill()

for i in range(3):
    b.forward(100)
    b.left(120)

b.end_fill()

# For Rectangle
b.penup()
b.goto(0, 0)
b.pendown()
b.color("white", "dark green")
b.begin_fill()

for i in range(2):
    b.forward(150)
    b.left(90)
    b.forward(80)
    b.left(90)

b.end_fill()

# For Hexagon 
b.penup()
b.goto(200, 0)
b.pendown()
b.color("white", "Dark blue")
b.begin_fill()

for i in range(6):
    b.forward(70)
    b.left(60)

b.end_fill()

# Finish
b.hideturtle()
turtle.done()
