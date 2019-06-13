import random, pylab


meanArrival = 60
arrivals = []
for i in range(2000):
    interArrivalTime = random.expovariate(1.0/meanArrival)
    arrivals.append(interArrivalTime)

ave = sum(arrivals)/len(arrivals)

xAxis = pylab.arange(0, len(arrivals), 1)

pylab.scatter(xAxis, arrivals)

pylab.axhline(meanArrival, linewidth=4, color="r")

pylab.title("Exponential Inter-arrival Time")
pylab.xlabel("Job Number #2000")
pylab.ylabel("Inter-arrival Time (secs)")

pylab.figure()
pylab.hist(arrivals)
pylab.title("Exponential Inter-arrival Time Histogram")
pylab.xlabel("Inter-arrival Time (secs)")
pylab.ylabel("Number of Jobs")

pylab.show()
