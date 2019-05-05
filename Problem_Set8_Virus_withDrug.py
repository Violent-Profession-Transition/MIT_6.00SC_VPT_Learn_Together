import numpy
import random
import pylab

"""from Problem_Set7"""
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
# PS7 PROBLEM 1 Implementing a Simple Simulation (No Drug Treatment) 
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

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        # inherits from SimpleVirus for maxBirthProb and clearProb
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        # unique attributes
        self.resistances = resistances
        self.mutProb = mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    
        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances[drug]


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a LIST of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # scan the drug in the List of drugs,
        # ONLY IF RESISTANT TO ALL DRUGS, can reproduce
        can_reproduce = True
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                can_reproduce = False

        # update the resistance dict based on mutProb
        # for each key of self.resistances, flip based on mutProb
        new_resistances = {}
        for key in self.resistances:
            # mutation probability will flip the resistance
            if random.random() <= (self.mutProb):
                new_resistances[key] = not self.resistances[key]
            else:
                new_resistances[key] = self.resistances[key]
                
        if can_reproduce and random.random() <= (self.maxBirthProb * (1-popDensity)):
            return ResistantVirus(
                self.maxBirthProb,
                self.clearProb,
                new_resistances,
                self.mutProb
            )
        else:
            raise NoChildException()


class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        SimplePatient.__init__(self, viruses, maxPop)
        # new attribute for Patient class, list of drugs
        self.drugs = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # should not allow one drug being added to the list multiple times
        if newDrug not in self.drugs:
            return self.drugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs        

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # for each virus in the self.viruses check for resistance in the drugResist list
        pop_resist = 0
        for virus in self.viruses:
            resist_all = True
            for drug in drugResist:
                if not virus.isResistantTo(drug):
                    resist_all = False
            if resist_all:
                pop_resist += 1
        return pop_resist
                   
    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        returns: the total virus population at the end of the update (an
        integer)
        """
        # 1. Determine whether each virus particle survives
        # and update the list of virus particles accordingly
        survived_viruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                survived_viruses.append(virus)
        # 2. The current population density is calculated.
        # This population density value is used until the next call to update().
        # defined as the current virus population
        # divided by the maximum population
        popDensity = float(len(survived_viruses))/self.maxPop
        # 3. Determine whether each virus particle should reproduce
        # and add offspring virus particles to the list of viruses in this patient. 
        # The list of drugs being administered should be accounted for in the
        # determination of whether each virus particle reproduces.
        offsprings = []
        for virus in survived_viruses:
            try:
                activeDrugs = self.getPrescriptions()
                virus_new = virus.reproduce(popDensity, activeDrugs)
                offsprings.append(virus_new)
            except NoChildException:
                continue

        # return the new virus population
        self.viruses = survived_viruses + offsprings
        return len(self.viruses)



# test for Problem1
"""
resistance_dict = {'guttagonol':False, 'grimpex': False}
v1 = ResistantVirus(0.99, 0.05, resistance_dict, 0.1)
for i in range(10):
    print(v1.doesClear())
virus_list = []
for i in range(5):
    virus_list.append(ResistantVirus(0.99, 0.05, resistance_dict, 0.1))
print("initial virus_list: ", virus_list)
p = Patient(virus_list, 1000)
p.addPrescription("guttagonol")
p.addPrescription("grimpex")
print(p.maxPop)
print(p.getPrescriptions())
print("initial virus population: ", p.getTotalPop())
for i in range(10):
    print("p.update() returns: ", p.update())
"""


#
# PROBLEM 2
#

def simulationWithDrug():
    """
    Runs simulations and plots graphs for problem 2.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    # viruses, a list of 100 ResistantVirus instances
    # maxPop, Maximum Sustainable Virus Population = 1000
    # Each ResistantVirus instance:
    # maxBirthProb, Maximum Reproduction Probability for a Virus Particle = 0.1
    # clearProb, Maximum Clearance Probability for a Virus Particle = 0.05
    # resistances, The virus's genetic resistance to drugs in the experiment = {guttagonol:False}
    # mutProb, Probability of a mutation in a virus particle's offspring = 0.005
    virus_list = []
    resistances = {"guttagonol":False}
    for i in xrange(100):
        virus_list.append(ResistantVirus(0.1, 0.05, resistances, 0.005))
    patient = Patient(virus_list, 1000)
    # simulates changes to
    # the virus population for 150 time steps
    # followed by the addition of the drug, guttagonol, followed by another 150 time steps
    virus_pop = [patient.getTotalPop()]
    gutta_resist_pop = [patient.getResistPop(['guttagonol'])]
    for i in xrange(150):
        virus_pop.append(patient.update())
        gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
        # print("len of virus_pop is: ", len(virus_pop))
    patient.addPrescription('guttagonol')
    # print("now patient has guttagonol prescribed: ", patient.getPrescriptions())
    for i in xrange(150):
        virus_pop.append(patient.update())
        gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
        # print("len of virus_pop is: ", len(virus_pop))
    # also return the guttagonol-resistant virus
    return virus_pop, gutta_resist_pop

"""
#### for plotting of problem2
virus_pop, gutta_resist_pop = simulationWithDrug()

# do 10 trials of simulation
numTrials = 10

total_virus_pop = [i*0 for i in xrange(301)]
mean_virus_pop = [i*0 for i in xrange(301)]
total_gutta_resist_pop = [i*0 for i in xrange(301)]
mean_gutta_resist_pop = [i*0 for i in xrange(301)]

for i in xrange(numTrials):
    virus_pop, gutta_resist_pop = simulationWithDrug()
    for x in xrange(301):
        total_virus_pop[x] += virus_pop[x]
        # print("total_virus_pop is now: ", total_virus_pop)
        total_gutta_resist_pop[x] += gutta_resist_pop[x]
        # print("total_gutta_resist_pop is now: ", total_gutta_resist_pop)
# print("total_virus_pop is now: ", total_virus_pop)
# print("total_gutta_resist_pop is now: ", total_gutta_resist_pop)

for j in xrange(301):
    mean_virus_pop[j] = float(total_virus_pop[j]) / numTrials
    mean_gutta_resist_pop[j] = float(total_gutta_resist_pop[j]) / numTrials
# print("mean_virus_pop is now: ", mean_virus_pop)
# print("mean_gutta_resist_pop is now: ", mean_gutta_resist_pop)

# pylab.plot need to appear in front of .legend
pylab.plot(range(301), mean_virus_pop, 'bo', label="Virus with drug after 150 steps")
pylab.title('Virus Population vs 150 no-drug and 150 with-drug Time Steps')
pylab.xlabel('Time Steps [step]')
pylab.ylabel('Virus Population [Num of viruses]')
# pylab.legend(loc='best')

pylab.plot(range(301), mean_gutta_resist_pop, 'ro', label="Gutta-Resistant Virus with drug after 150 steps")
# pylab.title('Gutta-Resistant Virus Population vs 150 no-drug and 150 with-drug Time Steps')
# pylab.xlabel('Time Steps [step]')
# pylab.ylabel('Gutta-Resistant Virus Population [Num of viruses]')
pylab.legend(loc='best')

pylab.show()
"""

#
# PROBLEM 3
#        

def simulationDelayedTreatment(delay=150):
    """
    Runs simulations and make histograms for problem 3.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).
    """
    # 300, 150, 75, and 0 time steps before administering guttagonol to the patient
    # 1. 300 + 150
    virus_list = []
    resistances = {"guttagonol":False}
    for i in xrange(100):
        virus_list.append(ResistantVirus(0.1, 0.05, resistances, 0.005))
    patient = Patient(virus_list, 1000)
    # simulates changes to
    # the virus population for DELAY time steps
    # followed by the addition of the drug, guttagonol, followed by another 150 time steps
    virus_pop = [patient.getTotalPop()]
    gutta_resist_pop = [patient.getResistPop(['guttagonol'])]
    # print("virus_pop is: ", virus_pop)
    # print("gutta_resist_pop is: ", gutta_resist_pop)
    for i in xrange(delay):
        virus_pop.append(patient.update())
        gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
        # print("len of virus_pop is: ", len(virus_pop))
        # print("virus_pop is: ", virus_pop)
        # print("gutta_resist_pop is: ", gutta_resist_pop)
    patient.addPrescription('guttagonol')
    # print("now patient has guttagonol prescribed: ", patient.getPrescriptions())
    for i in xrange(150):
        virus_pop.append(patient.update())
        gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
        # print("len of virus_pop is: ", len(virus_pop))
        # print("virus_pop is: ", virus_pop)
        # print("gutta_resist_pop is: ", gutta_resist_pop)
    # also return the guttagonol-resistant virus
    return virus_pop[delay+150], gutta_resist_pop[delay+150]
"""
numTrials = 30

after_300_total_virus_pop = []
after_300_total_gutta_resist_pop = []

for i in xrange(numTrials):
    virus_pop, gutta_resist_pop = simulationDelayedTreatment(300)
    after_300_total_virus_pop.append(virus_pop)
    print("total_virus_pop is now: ", after_300_total_virus_pop)
    # after_300_total_gutta_resist_pop.append(gutta_resist_pop)
    # print("total_gutta_resist_pop is now: ", after_300_total_gutta_resist_pop)

after_150_total_virus_pop = []
after_150_total_gutta_resist_pop = []

for i in xrange(numTrials):
    virus_pop, gutta_resist_pop = simulationDelayedTreatment(150)
    after_150_total_virus_pop.append(virus_pop)
    print("total_virus_pop is now: ", after_150_total_virus_pop)
    # after_150_total_gutta_resist_pop.append(gutta_resist_pop)
    # print("total_gutta_resist_pop is now: ", after_150_total_gutta_resist_pop)

after_75_total_virus_pop = []
after_75_total_gutta_resist_pop = []

for i in xrange(numTrials):
    virus_pop, gutta_resist_pop = simulationDelayedTreatment(75)
    after_75_total_virus_pop.append(virus_pop)
    print("total_virus_pop is now: ", after_75_total_virus_pop)
    # after_75_total_gutta_resist_pop.append(gutta_resist_pop)
    # print("total_gutta_resist_pop is now: ", after_75_total_gutta_resist_pop)

after_0_total_virus_pop = []
after_0_total_gutta_resist_pop = []

for i in xrange(numTrials):
    virus_pop, gutta_resist_pop = simulationDelayedTreatment(0)
    after_0_total_virus_pop.append(virus_pop)
    print("total_virus_pop is now: ", after_0_total_virus_pop)
    # after_0_total_gutta_resist_pop.append(gutta_resist_pop)
    # print("total_gutta_resist_pop is now: ", after_0_total_gutta_resist_pop)

fig, axs = pylab.subplots(2, 2)
# Remove horizontal space between axes
fig.subplots_adjust(hspace=0.6)

axs[0,0].hist(after_300_total_virus_pop)
axs[0,0].set_title('delay 300 steps')

axs[0,0].set_ylabel("Number of patients out of {}".format(numTrials))

axs[0,1].hist(after_150_total_virus_pop)
axs[0,1].set_title('delay 150 steps')

axs[1,0].hist(after_75_total_virus_pop)
axs[1,0].set_title('delay 75 steps')

axs[1,0].set_xlabel('Total virus population values')

axs[1,1].hist(after_0_total_virus_pop)
axs[1,1].set_title('delay 0 steps')

pylab.show()
"""

#
# PROBLEM 4
#
def simulationTwoDrugsDelayedTreatment(delay):
    """
    Runs simulations and make histograms for problem 4.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # new cocktail
    resistances = {'guttagonol':False, 'grimpex':False}
    # 300, 150, 75, and 0 time steps before administering guttagonol to the patient
    # 1. 300 + 150
    virus_list = []
    for i in xrange(100):
        virus_list.append(ResistantVirus(0.1, 0.05, resistances, 0.005))
    patient = Patient(virus_list, 1000)
    # simulates changes to
    # the virus population for DELAY time steps
    # followed by the addition of the drug, guttagonol, followed by another 150 time steps
    virus_pop = [patient.getTotalPop()]
    # gutta_resist_pop = [patient.getResistPop(['guttagonol', 'grimpex'])]
    # print("virus_pop is: ", virus_pop)
    # print("gutta_resist_pop is: ", gutta_resist_pop)
    for i in xrange(150):
        virus_pop.append(patient.update())
        # gutta_resist_pop.append(patient.getResistPop(['guttagonol', 'grimpex']))
        # print("len of virus_pop is: ", len(virus_pop))
        # print("virus_pop is: ", virus_pop)
        # print("gutta_resist_pop is: ", gutta_resist_pop)
    patient.addPrescription('guttagonol')
    # print("now patient has guttagonol prescribed: ", patient.getPrescriptions())
    for i in xrange(delay):
        virus_pop.append(patient.update())
        # gutta_resist_pop.append(patient.getResistPop(['guttagonol', 'grimpex']))
        # print("len of virus_pop is: ", len(virus_pop))
        # print("virus_pop is: ", virus_pop)
        # print("gutta_resist_pop is: ", gutta_resist_pop)
    patient.addPrescription('grimpex')
    for i in xrange(150):
        virus_pop.append(patient.update())
        # gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
        # print("len of virus_pop is: ", len(virus_pop))
        # print("virus_pop is: ", virus_pop)
        # print("gutta_resist_pop is: ", gutta_resist_pop)
    # also return the guttagonol-resistant virus
    return virus_pop[150+delay+150]#, gutta_resist_pop[delay+150]
"""
numTrials = 30

after_300_total_virus_pop = []
after_300_total_gutta_resist_pop = []

for i in xrange(numTrials):
    virus_pop = simulationTwoDrugsDelayedTreatment(300)
    after_300_total_virus_pop.append(virus_pop)
    print("total_virus_pop is now: ", after_300_total_virus_pop)
    # after_300_total_gutta_resist_pop.append(gutta_resist_pop)
    # print("total_gutta_resist_pop is now: ", after_300_total_gutta_resist_pop)

after_150_total_virus_pop = []
after_150_total_gutta_resist_pop = []

for i in xrange(numTrials):
    virus_pop = simulationTwoDrugsDelayedTreatment(150)
    after_150_total_virus_pop.append(virus_pop)
    print("total_virus_pop is now: ", after_150_total_virus_pop)
    # after_150_total_gutta_resist_pop.append(gutta_resist_pop)
    # print("total_gutta_resist_pop is now: ", after_150_total_gutta_resist_pop)

after_75_total_virus_pop = []
after_75_total_gutta_resist_pop = []

for i in xrange(numTrials):
    virus_pop = simulationTwoDrugsDelayedTreatment(75)
    after_75_total_virus_pop.append(virus_pop)
    print("total_virus_pop is now: ", after_75_total_virus_pop)
    # after_75_total_gutta_resist_pop.append(gutta_resist_pop)
    # print("total_gutta_resist_pop is now: ", after_75_total_gutta_resist_pop)

after_0_total_virus_pop = []
after_0_total_gutta_resist_pop = []

for i in xrange(numTrials):
    virus_pop = simulationTwoDrugsDelayedTreatment(0)
    after_0_total_virus_pop.append(virus_pop)
    print("total_virus_pop is now: ", after_0_total_virus_pop)
    # after_0_total_gutta_resist_pop.append(gutta_resist_pop)
    # print("total_gutta_resist_pop is now: ", after_0_total_gutta_resist_pop)

fig, axs = pylab.subplots(2, 2)
# Remove horizontal space between axes
fig.subplots_adjust(hspace=0.6)

axs[0,0].hist(after_300_total_virus_pop)
axs[0,0].set_title('gutta + delay 300 steps + grim')

axs[0,0].set_ylabel("Number of patients out of {}".format(numTrials))

axs[0,1].hist(after_150_total_virus_pop)
axs[0,1].set_title('delay 150 steps')

axs[1,0].hist(after_75_total_virus_pop)
axs[1,0].set_title('delay 75 steps')

axs[1,0].set_xlabel('Total virus population values')

axs[1,1].hist(after_0_total_virus_pop)
axs[1,1].set_title('delay 0 steps')

pylab.show()
"""
#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations(case):
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.
    """
    virus_list = []
    # new cocktail
    resistances = {'guttagonol':False, 'grimpex':False}
    for i in xrange(100):
        virus_list.append(ResistantVirus(0.1, 0.05, resistances, 0.005))
    patient = Patient(virus_list, 1000)

    virus_pop = [patient.getTotalPop()]
    gutta_resist_pop = [patient.getResistPop(['guttagonol'])]
    grim_resist_pop = [patient.getResistPop(['grimpex'])]

    for i in xrange(150):
        virus_pop.append(patient.update())
        gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
        grim_resist_pop.append(patient.getResistPop(['grimpex']))

    if case == 1:
        # case 1 gutta + 300 delay + grim + 150
        patient.addPrescription('guttagonol')
        # print("now patient has guttagonol prescribed: ", patient.getPrescriptions())
        for i in xrange(300):
            virus_pop.append(patient.update())
            gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
            grim_resist_pop.append(patient.getResistPop(['grimpex']))

        patient.addPrescription('grimpex')

        for i in xrange(150):
            virus_pop.append(patient.update())
            gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
            grim_resist_pop.append(patient.getResistPop(['grimpex']))

        return virus_pop, gutta_resist_pop, grim_resist_pop

    elif case == 2:
        # case 2 gutta+grim + 150
        patient.addPrescription('guttagonol')
        patient.addPrescription('grimpex')
        for i in xrange(150):
            virus_pop.append(patient.update())
            gutta_resist_pop.append(patient.getResistPop(['guttagonol']))
            grim_resist_pop.append(patient.getResistPop(['grimpex']))

        return virus_pop, gutta_resist_pop, grim_resist_pop

"""
# do 10 trials of simulation
numTrials = 10

###### case 1 150 + gutta + 300 delay + grim + 150
total_virus_pop = [i*0 for i in xrange(601)]
mean_virus_pop = [i*0 for i in xrange(601)]
total_gutta_resist_pop = [i*0 for i in xrange(601)]
mean_gutta_resist_pop = [i*0 for i in xrange(601)]
total_grim_resist_pop = [i*0 for i in xrange(601)]
mean_grim_resist_pop = [i*0 for i in xrange(601)]

for i in xrange(numTrials):
    virus_pop, gutta_resist_pop, grim_resist_pop = simulationTwoDrugsVirusPopulations(1)
    for x in xrange(601):
        total_virus_pop[x] += virus_pop[x]
        # print("total_virus_pop is now: ", total_virus_pop)
        total_gutta_resist_pop[x] += gutta_resist_pop[x]
        # print("total_gutta_resist_pop is now: ", total_gutta_resist_pop)
        total_grim_resist_pop[x] += grim_resist_pop[x]
        # print("total_grim_resist_pop is now: ", total_grim_resist_pop)
print("total_virus_pop is now: ", total_virus_pop)
print("total_gutta_resist_pop is now: ", total_gutta_resist_pop)
print("total_grim_resist_pop is now: ", total_grim_resist_pop)

for j in xrange(601):
    mean_virus_pop[j] = float(total_virus_pop[j]) / numTrials
    mean_gutta_resist_pop[j] = float(total_gutta_resist_pop[j]) / numTrials
    mean_grim_resist_pop[j] = float(total_grim_resist_pop[j]) / numTrials
print("mean_virus_pop is now: ", mean_virus_pop)
print("mean_gutta_resist_pop is now: ", mean_gutta_resist_pop)
print("mean_grim_resist_pop is now: ", mean_grim_resist_pop)

# pylab.plot need to appear in front of .legend
pylab.plot(range(601), mean_virus_pop, 'bo', label="Virus with drug after 150 steps")
pylab.title('Virus Population vs 150 no-drug and 300 with-gutta and 150 with grim Time Steps')
pylab.xlabel('Time Steps [step]')
pylab.ylabel('Virus Population [Num of viruses]')
# pylab.legend(loc='best')

pylab.plot(range(601), mean_gutta_resist_pop, 'ro', label="Gutta-Resistant Virus with drug after 150 steps")
# pylab.title('Gutta-Resistant Virus Population vs 150 no-drug and 150 with-drug Time Steps')
# pylab.xlabel('Time Steps [step]')
# pylab.ylabel('Gutta-Resistant Virus Population [Num of viruses]')
pylab.legend(loc='best')

pylab.plot(range(601), mean_grim_resist_pop, 'go', label="Grim-Resistant Virus with drug after 150+300 steps")
# pylab.title('Gutta-Resistant Virus Population vs 150 no-drug and 150 with-drug Time Steps')
# pylab.xlabel('Time Steps [step]')
# pylab.ylabel('Gutta-Resistant Virus Population [Num of viruses]')
pylab.legend(loc='best')

pylab.show()

###### case 2 150 + gutta|grim + 150
total_virus_pop = [i*0 for i in xrange(301)]
mean_virus_pop = [i*0 for i in xrange(301)]
total_gutta_resist_pop = [i*0 for i in xrange(301)]
mean_gutta_resist_pop = [i*0 for i in xrange(301)]
total_grim_resist_pop = [i*0 for i in xrange(301)]
mean_grim_resist_pop = [i*0 for i in xrange(301)]

for i in xrange(numTrials):
    virus_pop, gutta_resist_pop, grim_resist_pop = simulationTwoDrugsVirusPopulations(2)
    for x in xrange(301):
        total_virus_pop[x] += virus_pop[x]
        # print("total_virus_pop is now: ", total_virus_pop)
        total_gutta_resist_pop[x] += gutta_resist_pop[x]
        # print("total_gutta_resist_pop is now: ", total_gutta_resist_pop)
        total_grim_resist_pop[x] += grim_resist_pop[x]
        # print("total_grim_resist_pop is now: ", total_grim_resist_pop)
print("total_virus_pop is now: ", total_virus_pop)
print("total_gutta_resist_pop is now: ", total_gutta_resist_pop)
print("total_grim_resist_pop is now: ", total_grim_resist_pop)

for j in xrange(301):
    mean_virus_pop[j] = float(total_virus_pop[j]) / numTrials
    mean_gutta_resist_pop[j] = float(total_gutta_resist_pop[j]) / numTrials
    mean_grim_resist_pop[j] = float(total_grim_resist_pop[j]) / numTrials
print("mean_virus_pop is now: ", mean_virus_pop)
print("mean_gutta_resist_pop is now: ", mean_gutta_resist_pop)
print("mean_grim_resist_pop is now: ", mean_grim_resist_pop)

# pylab.plot need to appear in front of .legend
pylab.plot(range(301), mean_virus_pop, 'bo', label="Virus with drug after 150 steps")
pylab.title('Virus Population vs 150 no-drug and 150 with-gutta-grim Time Steps')
pylab.xlabel('Time Steps [step]')
pylab.ylabel('Virus Population [Num of viruses]')
# pylab.legend(loc='best')

pylab.plot(range(301), mean_gutta_resist_pop, 'ro', label="Gutta-Resistant Virus with drug after 150 steps")
# pylab.title('Gutta-Resistant Virus Population vs 150 no-drug and 150 with-drug Time Steps')
# pylab.xlabel('Time Steps [step]')
# pylab.ylabel('Gutta-Resistant Virus Population [Num of viruses]')
pylab.legend(loc='best')

pylab.plot(range(301), mean_grim_resist_pop, 'go', label="Grim-Resistant Virus with drug after 150 steps")
# pylab.title('Gutta-Resistant Virus Population vs 150 no-drug and 150 with-drug Time Steps')
# pylab.xlabel('Time Steps [step]')
# pylab.ylabel('Gutta-Resistant Virus Population [Num of viruses]')
pylab.legend(loc='best')

pylab.show()
"""