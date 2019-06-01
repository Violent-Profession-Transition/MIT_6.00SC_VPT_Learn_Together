import pylab, math, random
import scipy.integrate


"""
all the examples for both Monte Carlo by raindrop or
rectangular area are for y 0-1, x a-b
"""

def integrate_sine(f, a, b, step):
    """
    use raindrop method to estimate
    sine x
    """
    pylab.figure()
    yVals, xVals = [], []
    xVal = a
    while xVal <= b:
        xVals.append(xVal)
        yVals.append(f(xVal))
        xVal += step
    pylab.plot(xVals, yVals)
    pylab.title('sin(x)')
    pylab.xlim(a, b)
    xUnders, yUnders, xOvers, yOvers = [],[],[],[]
    for i in range(500):
        xVal = random.uniform(a, b)
        yVal = random.uniform(0, 1)
        if yVal < f(xVal):
            xUnders.append(xVal)
            yUnders.append(yVal)
        else:
            xOvers.append(xVal)
            yOvers.append(yVal)
    pylab.plot(xUnders, yUnders, 'go')
    pylab.plot(xOvers, yOvers, 'ko')
    pylab.xlim(a, b)
    ratio = len(xUnders)/(len(xUnders) + len(xOvers))
    print("ratio of drops inside the curve:", ratio)
    print("integral result for sinx: ", ratio*b)


integrate_sine(math.sin, 0, 1, 0.001)
pylab.show()

# Compare Monte Carlo by raindrop
# vs
# Monte Carlo by rectangular area

def integrate_by_drop(f, a, b, step):
    yVals, xVals = [], []
    xVal = a
    while xVal <= b:
        xVals.append(xVal)
        yVals.append(f(xVal))
        xVal += step
    Unders, Overs, = [],[]
    for i in range(500):
        xVal = random.uniform(a, b)
        yVal = random.uniform(0, 1)
        if yVal < f(xVal):
            Unders.append(xVal)
        else:
            Overs.append(xVal)
    ratio = len(Unders)/(len(Unders) + len(Overs))
    print("_------_for function: ", f.__name__)
    print("integral result from 0 to", b, ratio*b)


def integrate_by_rec(a,b,f,num_samples):
    y_sum = 0
    for sample in range(num_samples):
        # uniform sample between a and b
        # add the sum of all the ys
        y_sum += f(random.uniform(a,b))
    # average y is:
    average = y_sum / num_samples
    rect_area = average*(b-a)
    print("Integral by area for", f.__name__, rect_area)
    return rect_area

# f(x) = 1
def f_one(x):
    return 1

# f(x) = x
def f_x(x):
    return x

# f(x) = x**2
def f_xsquare(x):
    return x**2

integrate_by_drop(math.sin, 0, 1, 0.001)
integrate_by_drop(f_one, 0, 1, 0.001)
integrate_by_drop(f_x, 0, 1, 0.001)
integrate_by_drop(f_xsquare, 0, 1, 0.001)

integrate_by_rec(0, 1, math.sin, 1000)
integrate_by_rec(0, 1, f_one, 1000)
integrate_by_rec(0, 1, f_x, 1000)
integrate_by_rec(0, 1, f_xsquare, 1000)

print(scipy.integrate.quad(math.sin, 0, 1))
print(scipy.integrate.quad(lambda x: 1, 0, 1))
print(scipy.integrate.quad(lambda x: x, 0, 1))
print(scipy.integrate.quad(lambda x: x**2, 0, 1))
