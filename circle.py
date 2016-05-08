#Draws a circle via a 50 sided polygon using a Turtle; Includes Turtle setup 

import turtle

t = turtle

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
