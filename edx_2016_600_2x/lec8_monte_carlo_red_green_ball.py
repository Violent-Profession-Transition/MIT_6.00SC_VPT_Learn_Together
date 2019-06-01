import random

random.seed(0)

def pick3balls():
    # 3 red balls and 3 green balls
    balls = list("RRRGGG")
    picked = []
    for i in range(3):
        pick_ball = random.choice(balls)
        picked.append(pick_ball)
        balls.remove(pick_ball)
    return picked

#  print(pick3balls())

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    three_same = 0
    for trial in range(numTrials):
        res = pick3balls()
        print("picked 3 balls:", res)
        if res[0] == res[1] and res[1] == res[2]:
            three_same += 1
    print("Out of {} trials, {} are three same".format(numTrials, three_same))
    return three_same / numTrials


