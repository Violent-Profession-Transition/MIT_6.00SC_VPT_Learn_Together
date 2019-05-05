# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
"""design and implement a stochastic
simulation of patient and virus population dynamics
 and reach conclusions about treatment
regimens based on the simulation results
"""

"""Virus | drug treatment | computational models
Viruses such as HIV and H1N1 represent a significant challenge to modern medicine. One of the
reasons that they are so difficult to treat is because of their ability to evolve
--------
we will make use of simulations to explore the effect of introducing
drugs on the virus population and determine how best to address these treatment challenges
within a simplified model"""

"""
In this problem set, we will implement a
highly simplified stochastic model of virus population dynamics
"""

import numpy
import random
"""Random number generation isn't truly "random".
It is deterministic, and the sequence it generates is dictated by the
seed value you pass into random.seed
"""
import pylab


''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1 Implementing a Simple Simulation (No Drug Treatment) 
""" simulation of the spread of a virus
within a Person"""
#
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb


    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """
        return random.random() < self.clearProb


    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        # popDensity should be calculated in the
        # update method of the SimplePatient class
        if random.random() <= (self.maxBirthProb * (1-popDensity)):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException()



class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses  # list of virus instances
        self.maxPop = maxPop  # max virus population for this patient


    def getTotalPop(self):
        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.viruses)     


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        # 1. determine if virus particle survives and update virus list
        # print("before update, self.viruses: ", self.viruses)
        #print(">>>>>update the patient...")
        survived_viruses = []
        for virus in self.viruses:
            # if type(virus) == NoChildException:
            #     print("NoChildException")
            #     continue
            # elif not virus.doesClear():
            #     print("virus survived")
            #     new_viruses.append(virus)
            if not virus.doesClear():
                survived_viruses.append(virus)
        #print("self.viruses after update is: ", len(self.viruses))
        # 2. calculate current population density
        # defined as the current virus population
        # divided by the maximum population
        popDensity = float(len(survived_viruses))/self.maxPop
        #print("popDensity is: ", popDensity)
        # 3. reproduce the viruses and add offspring virus
        offsprings = []
        for virus in survived_viruses:
            try:
                virus_new = virus.reproduce(popDensity)
                # self.viruses.append(virus.reproduce(popDensity))
                offsprings.append(virus_new)
            except NoChildException:
                continue

        # return the new virus population
        self.viruses = survived_viruses + offsprings
        return len(self.viruses)

# test problem1
# v1 = SimpleVirus(0.99, 0.05)
# for i in range(10):
#     print(v1.doesClear())
# virus_list = []
# for i in range(5):
#     virus_list.append(SimpleVirus(0.99,0.05))
# print("initial virus_list: ", virus_list)
# p = SimplePatient(virus_list, 1000)
# print("initial virus population: ", p.getTotalPop())
# for i in range(10):
#     print("p.update() returns: ", p.update())

#
# PROBLEM 2
#
def simulationWithoutDrug():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    virus_list = []
    # maxBirthProb, Maximum Reproduction Probability for a Virus Particle = 0.1
    # clearProb, Maximum Clearance Probability for a Virus Particle = 0.05 
    for i in xrange(100):
        virus_list.append(SimpleVirus(0.1, 0.05))
    # simplePatient
    # viruses, a list of 100 SimpleVirus instances
    # maxPop, Maximum Sustainable Virus Population = 1000
    patient = SimplePatient(virus_list, 1000)
    # simulates changes to
    # the virus population for 300 time steps (i.e. 300 calls to update)
    virus_pop = [patient.getTotalPop()]
    for i in xrange(300):
        virus_pop.append(patient.update())
        # print("len of virus_pop is: ", len(virus_pop))
    return virus_pop

# do 10 trials of simulation
numTrials = 10
# total_pop = range(301)
# mean_pop = range(301)
total_pop = [i*0 for i in xrange(301)]
mean_pop = [i*0 for i in xrange(301)]
for i in xrange(numTrials):
    virus_pop = simulationWithoutDrug()
    for x in xrange(301):
        total_pop[x] += virus_pop[x]
print("total_pop is now: ", total_pop)

for j in xrange(301):
    mean_pop[j] = float(total_pop[j]) / numTrials
print("mean_pop is now: ", mean_pop)

# pylab.plot need to appear in front of .legend
pylab.plot(range(301), mean_pop, 'bo', label="Virus without drug")
pylab.title('Virus Population vs 300 Time Steps')
pylab.xlabel('Time Steps [step]')
pylab.ylabel('Virus Population [Num of viruses]')
pylab.legend(loc='best')


pylab.show()