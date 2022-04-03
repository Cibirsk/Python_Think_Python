plus_start = "+ - - - - +"
plus_end = " - - - - +"
pipe_start = "|         |"
pipe_end = "         |"


def print_line(value1, value2):
    print(value1, value2)


def print_four_line(value1, value2):
    print(value1, value2)
    print(value1, value2)
    print(value1, value2)
    print(value1, value2)


def print_carre(plus_start, plus_end, pipe_start, pipe_end):
    print_line(plus_start, plus_end)
    print_four_line(pipe_start, pipe_end)
    print_line(plus_start, plus_end)
    print_four_line(pipe_start, pipe_end)
    print_line(plus_start, plus_end)


print_carre(plus_start, plus_end, pipe_start, pipe_end)
