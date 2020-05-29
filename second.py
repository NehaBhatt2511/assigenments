import turtle
import math

second = turtle.Turtle()
second.color("blue","pink")
second.speed(100)
second.getscreen().bgcolor("black")

for i in range(50):
    second.color("pink")
    second.left(5)

    for j in range(5):
            second.color("blue")
            second.forward(10)
            second.left(150)
            second.circle(50)

            for k in range(5):
                second.forward(5)
                second.left(45)
                second.forward(10)



    



turtle.done()