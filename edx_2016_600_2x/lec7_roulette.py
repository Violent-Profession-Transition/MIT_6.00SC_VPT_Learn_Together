import random, pylab


class FairRoulette():
    """
    a fair roulette with no margin for bookkeeper
    Odds are fractional Odds, so not including the wager or stake
    Odds 1.0 = 1 to 1

    Black and Red numbers are laid out on a roulette wheel according
    to the isBlack method
    """
    def __init__(self):
        """
        pockets are the slots for the ball
        36 pockets
        """
        self.pockets = [p for p in range(1,37)]
        self.ball = None
        # Black Red Odds 1 to 1
        self.blackOdds, self.redOdds = 1.0, 1.0
        # Pocket Odds 35 to 1 for 36 pockets
        self.pocketOdds = len(self.pockets) - 1

    def spin(self):
        """chooses a pocket at random"""
        self.ball = random.choice(self.pockets)

    def isBlack(self):
        if type(self.ball) != int:
            return False
        # In number ranges from 1 to 10 and 19 to 28,
        # odd numbers are red and even are black.
        if (
            (self.ball>0 and self.ball<=10) or\
            (self.ball>18 and self.ball<=28)
            ):
            return self.ball%2 == 0 # even number black
        else:
            # In ranges from 11 to 18 and 29 to 36,
            # odd numbers are black and even are red.
            return self.ball%2 == 1 # odd number black
    def isRed(self):
        if type(self.ball) != int:
            return False
        return not self.isBlack()

    def betBlack(self, amt):
        """bet an amt on Black
        return the outcome as +- of amt
        """
        if self.isBlack():
            return amt*self.blackOdds # = amt
        else: return -amt
    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds # = amt
        else: return -amt

    def betPocket(self, pocket, amt):
        """bet an amt on which pocket"""
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else: return -amt

    def __str__(self):
        return "Fair Roulette"

def playRoulette(game, numSpins):
    luckyNumber = '2'
    bet = 1
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0
    for spin in range(numSpins):
        game.spin()  # spin the roulette
        totRed += game.betRed(bet)
        #  if game.betRed(bet) > 0:
            #  totRed += 1
        totBlack += game.betBlack(bet)
        #  if game.betBlack(bet) > 0:
            #  totBlack += 1
        totPocket += game.betPocket(luckyNumber, bet)
        #  if game.betPocket(luckyNumber, bet) > 0:
            #  totPocket += 1
    """
    print(numSpins, "spins of", game)
    print('Expected return betting red =',
          str(100*totRed/numSpins) + '%')
    print('Expected return betting black =',
          str(100*totBlack/numSpins) + '%')
    print('Expected return betting', luckyNumber, '=',
          str(100*totPocket/numSpins) + '%\n')
    """
    return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)


class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return 'American Roulette'

def findPocketReturn(game, numTrials, trialSize):
    """return a list of totPocket/numSpins
    trialSize = numSpins"""
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize)
        pocketReturns.append(trialVals[2])
    return pocketReturns

def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

#  random.seed(0)
numTrials = 20
resultDict = {}
games = [FairRoulette, EuRoulette, AmRoulette]

# init the resultDict with key-value key = name of roulette
# value = []
# map a game to a list of results for that game
for G in games:
    resultDict[G.__name__] = []

for numSpins in (100, 1000, 10000):
    print('\nSimulate betting a pocket on luckyNumber 2 for', numTrials,
          'trials of', numSpins, 'spins each')
    for G in games:
        pocketReturns = findPocketReturn(G(), numTrials, numSpins)
        mean, std = getMeanAndStd(pocketReturns)
        # store the result in resultDict
        resultDict[G.__name__].append((numSpins, 100*mean, 100*std))
        print('Expected return for', G(), '=',
             str(round(100*mean, 2)), "%")
        print("+/-", str(round(100*1.96*std, 3)), '%')
        print("with 95% confidence")

"""
resultDict after simulating numSpins and numTrials trials:
{'AmRoulette': [
    (100, 2.599999999999998, 47.31638194114169),
    (1000, -9.46, 18.50676633018313),
    (10000, -5.698000000000001, 5.651512717848204)],
 'EuRoulette': [
    (100, -8.200000000000001, 46.20779155077636),
    (1000, -2.44, 15.97442956728033),
    (10000, -4.096, 5.562436876046325)],
 'FairRoulette': [
    (100, 6.199999999999998, 77.60902009431635),
    (1000, 4.760000000000002, 20.23379351481081),
    (10000, -1.3060000000000003, 4.742274138005943)]}
"""
def plotReturn(resultDict):
    for roulette in resultDict:
        xVals, yVals, eVals = [], [], []
        for res in resultDict[roulette]:
            xVals.append(res[0])
            yVals.append(res[1])
            eVals.append(res[2])
        pylab.errorbar(xVals, yVals, yerr = eVals, label = roulette, marker = 'o')
    pylab.legend()
    pylab.xlabel('Spins per trial', fontsize = 'x-large')
    pylab.ylabel('Expected percentage return', fontsize = 'x-large')
    pylab.title('Expected Return Betting a Pocket', fontsize = 'x-large')
    pylab.semilogx()
    minX, maxX = pylab.xlim()
    pylab.xlim(1, maxX + 100000)

plotReturn(resultDict)
pylab.show()
