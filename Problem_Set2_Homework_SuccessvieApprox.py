# Problem #1
def evaluate_poly(poly, x):
    """
    computes the polynomial function for a given x
    return the computed value, type float
    E.g:
    poly = (0, 0, 5, 9.3, 7)
    f(x) = 5x^2 + 9.3x^3 + 7x^4
    x = -13
    f(-13) = 180339.9
    Type:
    poly: tuple, length>0
    x: number
    return: float
    """
    # initial result set to 0
    result = 0.0
    for index in range(len(poly)):
        result = result + poly[index] * x**index
    return result

assert(evaluate_poly((0,0,5), 2) == 20)
assert(evaluate_poly((0.5, 3.7, 1), -1) == -2.2)
assert(evaluate_poly((0,0,5,9.3,7), -13) == 180339.9)

# Problem #2
def compute_deriv(poly):
    """
    computes the derivative of a polynomial function
    if the derivative is 0, return (0.0, )
    E.g:
    poly = (-13.39, 0, 17.5, 3, 1)
    f(x) = -13.39 + 17.5x^2 + 3x^3 + x^4
    compute_deriv(poly) => 35x + 9x^2 + 4x^3 =>
    (0, 35, 9, 4)
    Type:
    poly: tuple of numbers, length > 0
    returns: tuple of number
    """
    # initial result is ()
    result = ()
    if len(poly) == 1:
        return (0.0, )
    for index in range(1,len(poly)):
        result = result + (poly[index]*index, )
    return result


assert(compute_deriv((2, )) == (0.0, ))
assert(compute_deriv((0, )) == (0.0, ))
assert(compute_deriv((3, 5, 7)) == (5, 14))
assert(compute_deriv((0, 0, -5, 0, 1)) == (0, -10, 0, 4))

# Problem #3 Newton approximation for root

def compute_root(poly, x_0, epsilon):
    """
    use Newton's method to find root of a polynomial function
    returns a tuple of (root, num_iteration)
    E.g.:
    poly = (-13.39, 0, 17.5, 3, 1)
    f(x) = -13.39x + 17.5x^2 + 3x^3 + x^4
    x_0 = 0.1
    epsilon = 0.0001
    compute_root(poly, x_0, epsilon) =>
    (0.8067907..., 8)
    Type:
    poly: tuple
    the polynomial function contains at least one real root
    x_0: float
    epsilon: float >0
    returns: tuple( float, int )
    """
    # initialize guess
    # x_0 is the first guess
    guess = x_0
    num_guess = 0
    while abs(evaluate_poly(poly, guess)) >= epsilon:
        guess = guess - evaluate_poly(poly, guess)/evaluate_poly(compute_deriv(poly), guess)
        num_guess += 1
    return (guess, num_guess)

assert((compute_root((-1, 1), 0.1, 0.0001)) == (1.0, 1))
assert((compute_root((-13.39, 0, 17.5, 3, 1), 0.1, 0.0001)) == (0.806790753796352, 7))
