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
    print(nbr_word)
    print(nbr_word_no_e)
    print('Il y a ' + str(pourcent_no_e) + ' % de mot sans e ')

def avoid(forbidden):
    fin = open('words2.txt')
    good_word = [] 
    bad_word = []
    for word in fin:
        for letter in word:
            if letter in forbidden:
                bad_word.append(word)
            else:
                good_word.append(word)
    print(good_word)
        
avoid("i")
