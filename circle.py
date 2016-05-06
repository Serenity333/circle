#Draws a circle via a 50 sided polygon using a Turtle; WARNING: Does NOT include Turtle set up. 

import math

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
