# Trace Anderson
# 4/15/26
# P4LAB1 - Extra Credit

import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # background color

# Create turtle
t = turtle.Turtle()
t.color("green")  # turtle (pen) color
t.pensize(2)

# Move turtle to starting position for square
t.penup()
t.goto(0, 0)
t.pendown()

# --- Draw square using a FOR loop ---
side_length = 100

for i in range(4):
    t.forward(side_length)
    t.right(90)

# Move to top-left of square
t.penup()
t.goto(0, 0)
t.pendown()

# --- Draw triangle using a WHILE loop ---
count = 0
while count < 3:
    t.forward(side_length)
    t.left(120)
    count += 1
    
    t.color("darkblue")
    t.begin_fill()

    # --- SUN ---
t.penup()              
t.goto(150, 150)      
t.pendown()           

t.color("yellow")     
t.begin_fill()
t.circle(40)         
t.end_fill()

# Finish
turtle.done()