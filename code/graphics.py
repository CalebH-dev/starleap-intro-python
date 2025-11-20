import turtle as t
import random

bob = t.Turtle()
bob.color('red', 'yellow')

# circle ish
# for i in range(1000):
#     bob.speed(0)
#     bob.left(i % 3 * 5) 
#     bob.forward(((i + 1) % 3) + (i * 3) % 4)
#     bob.right(i % 4 * 5)
#     bob.forward(i % 10)


# for i in range(100):
#     bob.forward(50)
#     bob.left(60)
#     bob.forward(50)
#     bob.right(88)

# var = True
# for i in range(1000):
#     bob.forward(50)
#     bob.lt(60)
#     bob.fd(50)
#     bob.lt(60)
#     bob.fd(50)
#     if var:
#         bob.right(120)
#     else: 
#         bob.right(60)

#     var = not var


def draw_gear(thing, angle):

    thing.lt(angle)
    for i in range(6):
        bob.forward(50)
        bob.lt(60)
        bob.forward(50)
        bob.rt(90)
        bob.forward(50)
        bob.lt(90)



bob.setpos(-50, -25)

draw_gear(bob, 0)

bob.setpos(-50, -25)
draw_gear(bob, 10)

bob.setpos(-50, -25)
draw_gear(bob, 20)


    




t.exitonclick() # Closes on click

