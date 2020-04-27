import turtle

BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
CHEESE_COLOR = "#FBC70F"
PEPPERONI_LOCATIONS = [
    [-70, 105],
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [20, 120],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150],
]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("My Pizza")

mt = turtle.Turtle()
mt.pensize(5)
mt.shape("circle")

def draw_circle(radius, line_color, fill_color):
    mt.color(line_color)
    mt.fillcolor(fill_color)
    mt.begin_fill()
    mt.circle(radius)
    mt.end_fill()

def move_turtle(x, y):
    mt.up()
    mt.goto(x, y)
    mt.down()

draw_circle(150, CRUST_COLOR, CRUST_COLOR)
move_turtle(0, 25)
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR)

for location in PEPPERONI_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)

move_turtle(0,150)
mt.color(BACKGROUND_COLOR)

for x in range (0,8):
    mt.pendown()
    mt.left(45)
    mt.forward(150)
    mt.penup()
    mt.backward(150)













turtle.done()
