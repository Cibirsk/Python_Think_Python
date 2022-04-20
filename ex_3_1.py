# Write a function named right_justify that takes a string named s as a parameter
# and prints the string with enough leading spaces so that the last letter of the
# string is in column 70 of the display.
# >>> right_justify('monty')
#                                                           monty

def right_justify(s):
    length = len(s)
    print(' ' * (70 - length) + s)


right_justify('monty')
right_justify('montyO')
right_justify('montyOO')
right_justify('montyOOO')
right_justify('montyOOOO')
