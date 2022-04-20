# 1. Draw a Koch curve with length x/3.
# 2. Turn left 60 degrees.
# 3. Draw a Koch curve with length x/3.
# 4. Turn right 120 degrees.
# 5. Draw a Koch curve with length x/3.
# 6. Turn left 60 degrees.
# 7. Draw a Koch curve with length x/3.

import turtle
bob = turtle.Turtle()


def koch2(t, x):
    if x < 3:
        t.fd(x)
    else:
        koch(t, x/3)
        t.fd(x/3)
        t.lt(60)
        t.fd(x/3)
        t.rt(120)
        t.fd(x/3)
        t.lt(60)
        t.fd(x/3)


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


koch(bob, 200)

turtle.mainloop()
