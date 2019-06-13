##It simulates a shuttle service in which a single
##bus serves a loop.  It starts with some generally useful
##classes for modeling queueing networks, and then uses some
##of them to build the bus simulation.


"""
NOTE: we are computing the average wait time of those passengers that get picked up
"""


import random, pylab, math
#  import time as pause


class Job:
    """Job has inter-arrival time,
    the work, the queue, the queue time"""
    def __init__(self, meanArrival, meanWork):
        #arrival rate of jobs, model as exponential
        self.arrival = random.expovariate(1.0/meanArrival)
        #time required to perform job, other distributions worth considering
        # model work as Gaussian
        self.wk = random.gauss(meanWork, meanWork/2.0)
        #Next attribute used to keep track of waiting time for job
        # Keep track of when a job enters the queue
        # so we can tell how long it had to wait
        self.timeQueued = None
    def interArrival(self):
        return self.arrival
    def work(self):
        return self.wk
    def queue(self, time):
        # init the time the job enters the queue
        self.timeQueued = time
    def queuedTime(self):
        return self.timeQueued

class Passenger(Job):
    """model the Passenger a Job,
    not adding anything new to Job class"""
    #Arrival rate is for passenger to arrive at bus stop
    #Work is time for passenger to board bus
    """ there are other things we could have done for work,
    like make it multi-dimensional: how long to get on the bus,
    how many stops etc"""
    # for simplicity, assume some agile people who just get
    # on the bus quickly, and some who are a bit slower,
    # and take longer time to get on the bus
    pass

class JobQueue:
    """Queues:
    Jobs can arrive, and the queue can
    have a length,
    NOTE: there is no implementation for
    jobs to leave the queue in this base class,
    each subclass will be distinguished by
    the queuing discipline it is using"""
    def __init__(self):
        self.jobs = []
    def arrive(self, job):
        """jobs arrive"""
        self.jobs.append(job)
    def length(self):
        return len(self.jobs)

class FIFO(JobQueue):
    """FIFO job discipline"""
    def depart(self):
        """
        each time a job needs to leave the queue,
        remove the 1st element in the queue
        """
        try:
            # pop the first element of the list
            return self.jobs.pop(0)
        except IndexError:
            print 'depart called with an empty queue'
            raise ValueError('EmptyQueue')

class LIFO(JobQueue):
    """LIFO job discipline"""
    def depart(self):
        """
        each time a job needs to leave the queue,
        remove the last element in the queue
        """
        try:
            # pop the first element of the list
            return self.jobs.pop(-1)
        except IndexError:
            print 'depart called with an empty queue'
            raise ValueError('EmptyQueue')

class SRPT(JobQueue):
    """SRPT allows for starvation, before it
    gets to be your turn, the bus is full and it leaves..."""
    def depart(self):
        """
        each time a job needs to leave the queue,
        search the queue to find one of th jobs
        with the least amount of work, and remove that
        """
        try:
            leastIndx = 0
            for i in range(len(self.jobs)):
                if self.jobs[i].work < self.jobs[leastIndx].work:
                    leastIndx = i
            return self.jobs.pop(leastIndx)
        except IndexError:
            print 'depart called with an empty queue'
            raise ValueError('EmptyQueue')

class BusStop(FIFO):
    """BusStop is a subclass of JobQueue
    you can make it a subclass of SRPT or anything subclass
    of JobQueue with a different queuing discipline
    """
    pass

class Bus:
    """our server is the bus
    every bus has:
    capacity (number of people it is allowed to hold)
    speed (how fast it goes from stop to stop)
    for simplicity we assume the speed only depends on
    the bus itself and not on the traffic
    also how many people are on the bus
    """
    def __init__(self, capacity, speed):
        self.cap = capacity
        self.speed = speed
        self.onBus = 0
    def getSpeed(self):
        return self.speed
    def getLoad(self):
        """return how many currently on the bus"""
        return self.onBus
    def enter(self):
        """people get on the bus,
        until it is full"""
        if self.onBus < self.cap:
            self.onBus +=1
        else:
            raise ValueError('full')
    def leave(self):
        """people alight the bus"""
        if self.onBus > 0:
            self.onBus -= 1
    def unload(self, num):
        """the actual method for unloading
        people from the bus
        unload num people from bus"""
        while num > 0:
            self.leave()
            num -= 1

def simBus(bus, numStops = 6, loopLen = 1200, meanArrival = 90,
           meanWork = 10, simTime = 1000):
    """
    Parameters:
        bus: only one bus, you have to wait for that first bus
        to get back from the loop
        numStops: number of stops in the loop
        loopLen: the loop length, assume the stops are equally
        spaced along the loop length
        meanArrival: the mean arrival rate of jobs
        meanWork: the mean work per job (time taken to get on bus)
        simTime: how long we are going to run the simulation
    Same unit for loop length and simulation time, so if we
    simulate for 30,000 times, and the loop is 1200 units long,
    this will tell us how many times around the loop
    we could get and how many stops the bus will make
    """
    assert loopLen%numStops == 0
    # create the bus stops
    stops = []
    for n in range(numStops):
        stops.append(BusStop())

    # initialize some variables to keep track
    # of performance
    time, totWait, totPassengers, lastArrival = [0.0]*4
    aveWaitTimes = []
    nextStop, busLoc, time = [0]*3

    # Passenger a subclass of Job
    nextJob = Passenger(meanArrival, meanWork)

    # Main iterations, while time not expired
    # ie how long we run the simulation
    while time < simTime:
        #  pause.sleep(0.1)
        #  print "time is now: ", time
        #advance time and move bus
        time += 1
        for i in range(bus.getSpeed()):
            busLoc += 1
            # has the bus driven
            # long enough to stop bus at bus stop
            if (busLoc)%(loopLen/numStops) == 0:
                print "****(BUS stop at a stop) *****"
                break  # stop moving the bus

        #see if there is a passenger waiting to enter queue
        # by checking the arrival timestamp
        # NOTE: the passenger (nextJob) can be arriving after several timesteps
        # in that case, this if branch doesnot get run
        if lastArrival + nextJob.interArrival() <= time:
            print "passengers at BusStop"
            #passengers arrive simultaneously at each stop
            for stop in stops:
                stop.arrive(nextJob)
            # init the time this Passenger
            # enters the queue
            nextJob.queue(time)
            lastArrival = time
            # create new instance of Passenger
            # Passengers arrive based on the characteristic
            # of the Job class
            nextJob = Passenger(meanArrival, meanWork)

        #see if bus is at a stop
        if (busLoc)%(loopLen/numStops) == 0:
            # First unload!
            # unload proportional to the num of Stops, like x//6
            # unload some fraction of the passengers
            print "~bus alight how many passenger? ", math.ceil(bus.getLoad()/float(numStops))
            bus.unload(math.ceil(bus.getLoad()/float(numStops)))

            # Then load passengers
            #all passengers who arrived prior to the bus's arrival
            #attempt to enter bus
            # while the BusStop has jobs(Passengers) waiting
            while stops[nextStop%numStops].length() > 0:
                try:
                    bus.enter()
                except:
                    # when bus is full, stop loading
                    #  print "BUS FULL!"
                    break
                # BusStop() depart method depends on the
                # JobQueue discipline
                p = stops[nextStop%numStops].depart()
                totWait += time - p.queuedTime()
                print "Total Wait is: ", totWait
                totPassengers += 1
                print "     for ", totPassengers, " passengers"
                # IMPT: adds the loading time to time!
                time += p.work() #advance time, but not bus
                print "Passenger took ", p.work(), " time to get on..."
            try:
                # aveWaitTimes is added each time the bus leaves a BusStop
                aveWaitTimes.append(totWait/totPassengers)
            except ZeroDivisionError:
                #  print "Zero passengers get on the bus at this stop"
                aveWaitTimes.append(0.0)
            #passengers might have arrived at stops while bus is loading
            # passengers arrive the same BusStop for the above while loop
            # do not get to enter the bus, will wait for next round
            # now time is time + p.work()
            while lastArrival + nextJob.interArrival() <= time:
                print ">>>new comers arrived while bus waiting"
                for stop in stops:
                    stop.arrive(nextJob)
                nextJob.queue(time)
                lastArrival += nextJob.interArrival()
                nextJob = Passenger(meanArrival, meanWork)
            # if bus at bus stop, now bus done with this bus stop
            nextStop += 1
            print "@@@@@@ Done with this but stop@@@@@"

        # end of time < simTime iterations

    # keep track of the people left waiting
    # when the simulation ends
    leftWaiting = 0
    for stop in stops:
        leftWaiting += stop.length()

    # aveWaitTimes is the list of waiting times after each BusStop
    return aveWaitTimes, leftWaiting

def test(capacities, speeds, numTrials):
    """
    run simBus() multiple times, accumulate
    results from trials and then plot them
    for first 500 stops in the looping
    combinations of speeds and capacities
    """
    random.seed(0)
    for cap in capacities:
        for speed in speeds:
            #  totWaitTimes = pylab.array([0.0]*500) #keep track of 1st 500 stops
            totWaitTimes = pylab.array([0.0]*200)
            totLeftWaiting = 0.0
            for t in range(numTrials):
                aveWaitTimes, leftWaiting = simBus(Bus(cap, speed))
                print "len of aveWaitTimes is: ", len(aveWaitTimes)
                #  print aveWaitTimes
                # totWaitTimes is accumulative since aveWaitTimes is accumulative
                totWaitTimes += pylab.array(aveWaitTimes[:200])
                totLeftWaiting += leftWaiting
            # get the average after numTrials
            aveWaitTimes = totWaitTimes/numTrials
            leftWaiting = int(totLeftWaiting/numTrials)
            lab = 'Bus-Capacity = ' + str(cap) + ', Speed = ' + str(speed) + ', LeftWaiting = ' + str(leftWaiting)
            pylab.plot(aveWaitTimes, 'go', label=lab)

    pylab.xlabel('Bus-Stop Number')
    pylab.ylabel('Aggregate Average Wait Time')
    pylab.title('Impact of Bus Speed and Capacity {}'.format(type_queue))
    ymin, ymax = pylab.ylim()
    #  if ymax - ymin > 200:
        #  pylab.semilogy()
    pylab.ylim(ymin=ymin, ymax=ymax)
    pylab.legend(loc='best')

type_queue = "FIFO"

# test(capacities, speeds, numTrials):
test([1], [0], 10)
#  test([15], [10], 10) ## capacity of 15, speed of 10
#  test([18], [10], 10)
#  test([19], [10], 10)
#  #  test([15], [20], 10) ## capacity of 15, speed of 20
#  test([20], [10], 10)
#  test([30], [10], 10) ## capacity of 30, speed of 10
#  test([15, 30], [6, 10, 20], 20)
pylab.show()
