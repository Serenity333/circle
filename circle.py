#Draws a circle via a 50 sided polygon using a Turtle; WARNING: Does NOT include Turtle set up. 
#Requires polygon script

import math *

import polygon

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
