import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    number = random.randint(10, 20)

    while (number % 2 != 0):
        number = random.randint(10, 20)

    return number
