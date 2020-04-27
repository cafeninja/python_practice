import turtle

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Drawing Lines Practice")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")
my_turtle.forward(100)

for x in range(0,8):
    my_turtle.forward(100)
    my_turtle.backward(100)
    my_turtle.left(45)

my_turtle.hideturtle()
turtle.done()
    
##my_turtle.left(45)
##my_turtle.penup()
##my_turtle.forward(100)
##my_turtle.pendown()
##my_turtle.forward(100)
##my_turtle.backward(100)

