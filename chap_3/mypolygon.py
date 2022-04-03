import turtle
bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(turtle, length, nbr_side):
    for i in range(nbr_side):
        turtle.fd(length)
        turtle.lt(360/nbr_side)  # calcul l'angle selon nbr cotés


def circle(t, r):
    long_totale = (r*2*3.14)
    nbr_side = 100
    polygon(bob, long_totale/nbr_side, nbr_side)


def arc(t, r, angle):
    long_totale = (r*2*3.14)
    nbr_side = 100

    for i in range(angle):
        turtle.fd(long_totale/nbr_side)
        turtle.lt(360/nbr_side)  # calcul l'angle selon nbr cotés


circle(bob, 100)
#arc(bob, 100, 180)


turtle.mainloop()
