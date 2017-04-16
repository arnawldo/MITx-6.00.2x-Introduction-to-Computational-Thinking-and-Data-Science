import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    for number in range(9, 21):
        if number % 2 ==0:
            return number
