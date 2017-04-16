import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    number = random.randrange(0, 100)

    while (number % 2 != 0):
        number = random.randrange(0, 100)

    return number