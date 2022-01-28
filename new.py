import turtle
import math

new = turtle.Turtle()
new.color("blue")
new.speed(100)

for i in range(100):
    new.forward(300)
    new.left(170)
    new.circle(50)
    new.forward(20)
    new.left(math.cos(i)*10)
    
    




turtle.done()