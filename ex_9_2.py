def has_no_e():
    fin = open('words.txt')
    nbr_word = 0
    nbr_word_no_e = 0
    for line in fin:
        nbr_word += 1
        word = line.strip()
        if 'e' not in word:
            nbr_word_no_e += 1
            print(word)
    pourcent_no_e = int(nbr_word_no_e / nbr_word * 100)
    print('Il y a ' + str(pourcent_no_e) + ' % de mot sans e ')

has_no_e()