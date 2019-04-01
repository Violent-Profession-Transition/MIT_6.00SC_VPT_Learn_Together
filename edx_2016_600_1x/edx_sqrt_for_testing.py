def sqrt(x, eps):
    """
    Assumes x, eps floats, x >=0, eps >0
    Returns result such that x - eps <= result **2 <= x + eps
    """
    """
    newton-raphson is an algorithm to find the root to a polynomial function
    for any guess, a better guess is guess - f(guess)/f'(guess)
    """
    # first check if x is 0:
    if x == 0:
        return 0
    guess = x/2
    print("now guess is: ", guess)
    while guess**2 > (x + eps) or guess**2 < (x - eps):
        # implement newton raphson algorithm
        guess = guess - (guess**2 - x)/(2*guess)
        print("now guess is: ", guess)
    return guess

#  print(sqrt(0, 0.01))
#  print(sqrt(1, 0.01))
#  print(sqrt(2, 0.01))
#  print(sqrt(0.25, 0.01))
#  print(sqrt(25, 0.01))

def sqrt_bisection_search(x, eps):
    """
    Assumes x, eps floats, x >=0, eps >0
    Returns result such that x - eps <= result **2 <= x + eps
    """
    # first check if x is 0:
    if x == 0:
        return 0
    # use bisection search
    # initialize the upper and lower bound
    upper_bound = x
    lower_bound = 0
    # first detect if x is smaller than 1
    # change upper_bound to 1
    if x < 1:
        upper_bound = 1
        lower_bound = x
    guess = (upper_bound + lower_bound) / 2
    while guess**2 > (x + eps) or guess**2 < (x - eps):
        print("upper_bound", upper_bound, "lower_bound", lower_bound)
        mid = (upper_bound + lower_bound) / 2
        if guess**2 > (x + eps):
            upper_bound = mid
        else:
            lower_bound = mid
        # new guess at the mid of new upper and lower bounds
        guess = (upper_bound + lower_bound) / 2
    return guess

print(sqrt_bisection_search(2, 0.01))
print(sqrt_bisection_search(25, 0.01))
print(sqrt_bisection_search(0.25, 0.01))

