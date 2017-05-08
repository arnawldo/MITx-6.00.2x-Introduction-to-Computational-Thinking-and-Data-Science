def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''

    import random

    # number of times 3 same colour balls were collected
    same_number = 0

    # run trials
    for _ in range(numTrials):
        # bucket of balls, 4 red, 4 green
        bucket = (['R'] * 4) + (['G'] * 4)
        # picked balls
        picked = []
        # three picks
        for _ in range(3):
            # pick ball at random from basket and store in picked
            position = random.choice(range(len(bucket))) # index of picked ball
            picked.append(bucket.pop(position))
        # if balls in picked are similar, success
        if len(set(picked)) <= 1:
            same_number += 1

    # success rate
    success_rate = same_number / numTrials

    return success_rate

if __name__ == '__main__':
    # test function for increasing number of trials
    # answer close to 0.143

    import pylab

    numtrials = range(10, 10000, 1000)
    estimates = []

    for ntrials in numtrials:
        estimates.append(drawing_without_replacement_sim(ntrials))

    pylab.plot(numtrials, estimates)
    pylab.title('Estimated probability of 3 same colour balls')
    pylab.show()
