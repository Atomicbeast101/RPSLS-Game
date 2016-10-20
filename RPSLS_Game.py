# =================================================================== #
#                Rock|Paper|Scissors|Lizard|Spock Game                #
#                Developed by Atomicbeast101 (Github)                 #
#                                                                     #
#  Win # Info:                                                        #
#    -1 = User wins                                                   #
#     0 = Tie between user and computer                               #
#     1 = Computer wins                                               #
# =================================================================== #

import random

accLttrs = ['R', 'P', 'S', 'L', 'K', 'N']
compOptns = ['R', 'P', 'S', 'L', 'K']


def getwin(usr, cpt):
    if usr == 'R':
        if cpt == 'R':
            return 'rock', 'rock', 0, ''
        if cpt == 'P':
            return 'rock', 'paper', 1, 'covers'
        if cpt == 'S':
            return 'rock', 'scissors', -1, 'crushes'
        if cpt == 'L':
            return 'rock', 'lizard', -1, 'crushes'
        if cpt == 'K':
            return 'rock', 'spock', 1, 'vapourises'
    if usr == 'P':
        if cpt == 'R':
            return 'paper', 'rock', -1, 'covers'
        if cpt == 'P':
            return 'paper', 'paper', 0, ''
        if cpt == 'S':
            return 'paper', 'scissors', 1, 'cuts'
        if cpt == 'L':
            return 'paper', 'lizard', 1, 'eats'
        if cpt == 'K':
            return 'paper', 'spock', -1, 'disaproves'
    if usr == 'S':
        if cpt == 'R':
            return 'scissors', 'rock', 1, 'crushes'
        if cpt == 'P':
            return 'scissors', 'paper', -1, 'cuts'
        if cpt == 'S':
            return 'scissors', 'scissors', 0, ''
        if cpt == 'L':
            return 'scissors', 'lizard', -1, 'decapitates'
        if cpt == 'K':
            return 'scissors', 'spock', 1, 'smashes'
    if usr == 'L':
        if cpt == 'R':
            return 'lizard', 'rock', 1, 'crushes'
        if cpt == 'P':
            return 'lizard', 'paper', -1, 'eats'
        if cpt == 'S':
            return 'lizard', 'scissors', 1, 'decapitates'
        if cpt == 'L':
            return 'lizard', 'lizard', 0, ''
        if cpt == 'K':
            return 'lizard', 'spock', -1, 'poisons'
    if usr == 'K':
        if cpt == 'R':
            return 'spock', 'rock', -1, 'vapourises'
        if cpt == 'P':
            return 'spock', 'paper', 1, 'disaproves'
        if cpt == 'S':
            return 'spock', 'scissors', -1, 'smashes'
        if cpt == 'L':
            return 'spock', 'lizard', 1, 'poisons'
        if cpt == 'K':
            return 'spock', 'spock', 0, ''

cont = True
while cont:
    print 'Options:'
    print '\t[R] - Rock'
    print '\t[P] - Paper'
    print '\t[S] - Siccors'
    print '\t[L] - Lizard'
    print '\t[K] - Spock'
    print '\t[N] - Close Program\n'
    inp = raw_input('Choose your fate (R, P, S, L, K, or N): ')[0].upper()
    if inp in accLttrs:
        if inp != 'N':
            val = compOptns[random.randint(0, 4)]
            print inp + ' - ' + val
            user, cptr, win, rsn = getwin(inp, val)
            if win == -1:
                print '\t     You chose: ' + user
                print '\tComputer chose: ' + cptr
                print 'Looks like you won! Because ' + user + ' ' + rsn + ' ' + cptr + '!'
            elif win == 0:
                print 'You chose ' + user + ' while the computer chose ' + cptr + '. Looks like its a tie!'
            else:
                print '\t     You chose: ' + user
                print '\tComputer chose: ' + cptr
                print 'Looks like you lost! Because ' + cptr + ' ' + rsn + ' ' + user + '!'
        else:
            print 'Thank you for playing the game! Closing game...'
            cont = False
    else:
        print 'Invalid input ' + inp + ' please try again!'
