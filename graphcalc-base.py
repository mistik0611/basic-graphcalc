# A graph calculator with only limited functions

import turtle
import math

# Get user input for x and y-axis length
xLen = 10 #int(input("Enter x-axis length: "))
yLen = 8  #int(input("Enter y-axis length: "))

# Constant variables for objects
graph = turtle.Turtle()
xAxis = turtle.Turtle()
yAxis = turtle.Turtle()
screen = turtle.Screen()

# Set up screen
screen.title("Graphing Calculator")
screen.screensize(640, 480) # Add more options
screen.bgcolor("white")

# Draw x-axis
xAxis.hideturtle()
xAxis.penup()
xAxis.speed(0)
xAxis.goto(-300, 0)
xAxis.pendown()
xStep = (300 - (300 % xLen)) / xLen
for i in range(xLen*2): # Draw step lines for x-axis
    xAxis.forward(xStep)
    xAxis.left(90)
    xAxis.forward(5)
    xAxis.backward(10)
    xAxis.forward(5)
    xAxis.right(90)
xAxis.penup()
xAxis.home()

# Draw y-axis
yAxis.hideturtle()
yAxis.penup()
yAxis.speed(0)
yAxis.goto(0, -240)
yAxis.left(90)
yAxis.pendown()
yStep = (240 - (240 % yLen)) / yLen
for i in range(yLen*2): # Draw step lines for y-axis
    yAxis.forward(yStep)
    yAxis.left(90)
    yAxis.forward(5)
    yAxis.backward(10)
    yAxis.forward(5)
    yAxis.right(90)
yAxis.penup()
yAxis.home()

# Reset turtle to draw graph
graph.penup()

# Function to plot points of graph
def plot(x, y):
    graph.goto(x, y)
    graph.pendown()
    graph.dot(4)

# Linear function graph
def linear(a, b):
    graph.pencolor("red")
    for x in range(-300, 300, int(xStep)):
        y = (a * x) + (b * yStep)
        plot(x, y)
    graph.penup()

# Quadratic function graph
def quad(a, b, c):
    graph.pencolor("blue")
    for x in range(int(-120 + (b*xStep)), int(121 - (b*xStep)), int(xStep)):
        y = (a * ((x*x)/xStep)) + (b * x) + (c * xStep)
        plot(x, y)
    graph.penup()

# Cubic function graph
def cubic(a, b, c, d):
    graph.pencolor("green")
    for x in range(-90, 91, int(xStep)): # Need to shift range when the graph shifts
        y = (a * ((x*x*x)/(yStep*yStep))) + (b * ((x*x)/yStep)) + (c * x) + (d * yStep)
        plot(x, y)
    graph.penup()

# Square root function graph
def sqroot():
    graph.pencolor("cyan")
    for x in range(20):
        y = math.sqrt(x)
        plot((x * xStep), (y * yStep))
    graph.penup()

# Cube root function graph
def cbroot():
    graph.pencolor("lawngreen")
    for x in range(-20, 20):
        y = math.cbrt(x)
        plot((x * xStep), (y * yStep))
    graph.penup()

# Exponential function graph
def expnt(base=math.e):
    graph.pencolor("magenta")
    for x in range(-20, 5):
        y = math.pow(base, x)
        plot((x * xStep), (y * yStep))
    graph.penup()

# Logarithmic function graph
def logrtm(base=math.e):
    graph.pencolor("coral")
    for x in range(1, 10):
        y = math.log((x/1000), base)
        plot(((x/1000) * xStep), (y * yStep))
    for x in range(10, 100, 10):
        y = math.log((x/1000), base)
        plot(((x/1000) * xStep), (y * yStep))
    for x in range(100, 1000, 100):
        y = math.log((x/1000), base)
        plot(((x/1000) * xStep), (y * yStep))
    for x in range(1000, 20000, 1000):
        y = math.log((x/1000), base)
        plot(((x/1000) * xStep), (y * yStep))
    graph.penup()

# Sine function graph
def sinx():
    graph.pencolor("green")
    for x in range(-10, 11):
        y = math.sin(x)
        plot((x * xStep), (y * yStep))
    graph.penup()

# Cosine function graph
def cosx():
    graph.pencolor("blue")
    for x in range(-10, 11):
        y = math.cos(x)
        plot((x * xStep), (y * yStep))
    graph.penup()

# Tangent function graph
def tanx():
    graph.pencolor("red")
    for x in range(-10, 11):
        y = math.tan(x)
        plot((x * xStep), (y * yStep))
    graph.penup()


"""linear(3, 5)
quad(1, -4, 3)
cubic(1, 0, 0, 0) # Needs rework
sqroot()
cbroot()
expnt()
logrtm()"""
sinx()
cosx()

turtle.done()
