import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''

    success_count = 0

    for _ in range(numTrials):

        bucket = ['R']*3 + ['G']*3 # ['R','R','R','G','G','G']
        drawn_balls = []

        for _ in range(3):
            # drawing three times
            random_bucket_index = random.randrange(0, len(bucket))
            drawn_ball = bucket.pop(random_bucket_index)
            drawn_balls.append(drawn_ball)

        if (drawn_balls == ['R']*3) or (drawn_balls == ['G']*3):
            success_count += 1

    return success_count / numTrials

# test function on 100000 trials
# print(noReplacementSimulation(100000))