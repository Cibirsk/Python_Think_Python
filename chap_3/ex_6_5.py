# A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
# function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
# you will have to think about the base case.

def is_power(a, b):

    if a % b == 0:
        a = a/b
        if is_power(a/b, b):
            return True
    return False


print(is_power(2, 1))
