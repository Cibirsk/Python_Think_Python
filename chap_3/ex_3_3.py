def plus_trait():
    print('+', 4*' - ', '+', 4*' - ', end=' ')


def pipe_space():
    print('|', 12*' ', '|', 12*' ', end=' ')


def deux_lignes(f, separ):
    f()
    print(separ)


def do_four(f, separ):
    f()
    print(separ)
    f()
    print(separ)
    f()
    print(separ)
    f()
    print(separ)


deux_lignes(plus_trait, '+')
do_four(pipe_space, '|')
deux_lignes(plus_trait, '+')
do_four(pipe_space, '|')
deux_lignes(plus_trait, '+')
