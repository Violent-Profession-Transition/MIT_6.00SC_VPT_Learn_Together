import random, pylab

def montyChoose(guessDoor, prizeDoor):
    """
    Monty open the remaining door that does not
    contain the prize
    """
    if guessDoor != 1 and prizeDoor != 1:
        return 1
    elif guessDoor != 2 and prizeDoor != 2:
        return 2
    elif guessDoor != 3 and prizeDoor != 3:
        return 3

def simMontyHall(numTrials = 100, chooseFcn = montyChoose):
    stickWins = 0
    switchWins = 0
    noWin = 0
    prizeDoorChoices = [1, 2, 3]
    guessChoices = [1, 2, 3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guessDoor = random.choice([1, 2, 3])
        print("guessDoor is: ", guessDoor)
        toOpen = chooseFcn(guessDoor, prizeDoor)
        print("Monty opened: ", toOpen)
        switchDoor = [i for i in guessChoices if i not in (guessDoor, toOpen)]
        if guessDoor == prizeDoor:
            stickWins += 1
            print("sitck wins!")
        elif switchDoor[0] == prizeDoor:
            switchWins += 1
            print("Switch wins!!")
    return (stickWins, switchWins)

def displayMHSim(simResults):
    stickWins, switchWins = simResults
    pylab.pie(
        [stickWins, switchWins],
        colors=['r','g'],
        labels = ['stick', 'change'],
        autopct = '%.2f%%'
    )
    pylab.title('To Switch or Not to Switch')

displayMHSim(simMontyHall(10, montyChoose))
pylab.show()