import random, pylab


# You are given this function
def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)


# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """

    longest_runs = []

    # run trials
    for _ in range(numTrials):
        # longest run seen so far in single trial
        longest_run = 1
        # current moving run
        moving_run = 1
        on_a_roll = False
        # start rolling die
        for i in range(numRolls):
            # for first roll, no calculations needed
            if i == 0:
                previous_roll = die.roll()
                continue
            current_roll = die.roll()
            # if previous and current rolls are similar
            if current_roll == previous_roll:
                moving_run += 1
                on_a_roll = True
                longest_run = max(longest_run, moving_run)
                # reassignment of previous roll not needed, since its already similar to current
                continue
            # if previous and current rolls are not similar
            if on_a_roll:
                # if was on a run, cancel run and restart run counter
                previous_roll = current_roll
                on_a_roll = False
                moving_run = 1
                continue
            # if not on run
            previous_roll = current_roll

        longest_runs.append(longest_run)

    # make histogram of runs
    makeHistogram(longest_runs, numBins=10, xLabel='longest run', yLabel='count')

    mean_longest_run = getMeanAndStd(longest_runs)[0]
    # rounded to 3 decimal places
    mean_longest_run = round(mean_longest_run, 3)
    return mean_longest_run


# One test case
print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 500, 10000))
