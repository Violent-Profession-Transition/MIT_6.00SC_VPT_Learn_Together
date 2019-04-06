"""You flip a fair coin 3 times, write down the probability
of the below events. Assume all sequences are equally likely
"""

import random

# 1. Three heads: A : {H,H,H}
def flipCoin():
    """randomly return a Head or Tail"""
    return random.choice(["H", "T"])

def flipThreeTimes():
    """flip a coin three times"""
    result = ''
    for i in range(3):
        result += flipCoin()
    return result

threeH = 0
HTH = 0
any_2H1T = 0
any_HgtT = 0
for trial in range(10000):
    outcome = flipThreeTimes()
    if outcome == "HHH":
        threeH += 1
        any_HgtT += 1
    elif outcome == "HTH":
        HTH += 1
        any_2H1T += 1
        any_HgtT += 1
    elif outcome == "HHT" or outcome == "THH":
        any_2H1T += 1
        any_HgtT += 1

print("probability of getting three heads is: ", float(threeH)/10000)

# 2. The sequence head, tail, head: A : {H,T,H}
print("probability of getting HTH is: ", float(HTH)/10000)

# 3. Any sequence with 2 heads and 1 tail
print("probability of getting any sequence with 2 heads and 1 tail is: ", float(any_2H1T)/10000)

# 4. Any sequence where the number of heads is greater than or equal to the number of tails
print("probability of getting any sequence with H greater than T is: ", float(any_HgtT)/10000)

"""2. What is the probability of rolling a Yahtzee! on the first roll?
That is, what is the probability of rolling five 6-sided dice,
and having them all display the same number?"""

def rollDie():
    """return 1-6 of the dice"""
    return random.choice([1,2,3,4,5,6])

def rollYahtzee():
    """roll 5 dice together"""
    result = ''
    for i in range(5):
        result += str(rollDie())
    return result

def detectYahtzee(result):
    """return True if all 5 dice have same number"""
    # use string.count()
    return result.count(result[0]) == len(result)
    

yahtzee = 0
for trial in range(10000):
    result = rollYahtzee()
    if detectYahtzee(result):
        yahtzee += 1
print("probability of getting Yahtzee is: ", float(yahtzee)/10000)

