"""
newton-raphson is an algorithm to find the root to a polynomial function
for any guess, a better guess is guess - f(guess)/f'(guess)
"""

# for function f(x) = x^2 - 24

# epsilon is acceptable range of error
epsilon = 0.01
# num_Guess is number of attempted guesses
num_Guess = 0

# initial guess start with half the value of k = 24
guess = 24 / 2

print("start guess with: ", guess)

while (guess**2 - 24) >= epsilon:
    # a better guess will be:
    guess = guess - (guess**2 - 24)/(2*guess)
    print("now guess is: ", guess)
    num_Guess += 1
    print("# of attempted guesses is: ", num_Guess)

# output the result
print("Square root of 24 is about ", guess)
