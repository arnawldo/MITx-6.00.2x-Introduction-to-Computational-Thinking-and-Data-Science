import random, pylab

xVals = []
yVals = []
wVals = []

for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())

xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)

xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

# distribution of tVals
pylab.hist(tVals)
pylab.title('tVals')
pylab.show()
# distribution of xVals
pylab
pylab.hist(xVals)
pylab.title('xVals')
pylab.show()
# plot of xVals vs zVals
pylab.plot(xVals, zVals)
pylab.title('xVals vs zVals')
pylab.show()
# plot of xVals vs yVals
pylab.plot(xVals, yVals)
pylab.title('xVals vs yVals')
pylab.show()
# plot of xVals vs sorted yVals
pylab.plot(xVals, sorted(yVals))
pylab.title('xVals vs sorted yVals')
pylab.show()
# plot of sorted xVals vs yVals
pylab.plot(sorted(xVals), yVals)
pylab.title('sorted xVals vs yVals')
pylab.show()
# plot of sorted xVals vs sorted yVals
pylab.plot(sorted(xVals), sorted(yVals))
pylab.title('sorted xVals vs sorted yVals')
pylab.show()