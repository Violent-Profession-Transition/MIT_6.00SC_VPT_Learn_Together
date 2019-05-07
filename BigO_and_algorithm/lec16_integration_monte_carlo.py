import pylab, random


def integrate(a,b,f,num_samples):
    y_sum = 0
    for sample in range(num_samples):
        # uniform sample between a and b
        # add the sum of all the ys
        y_sum += f(random.uniform(a,b))
    # average y is:
    average = y_sum / num_samples
    rect_area = average*(b-a)
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

integrate_1 = integrate(1,2,f_one,1000) # 1
integrate_x = integrate(1,2,f_x,1000) # 1.5028872692289563
integrate_xsquare = integrate(1,2,f_xsquare,1000) # 2.33620877892123

def doubleIntegrate(a, b, c, d, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        pinSum += f(x, y)
    average = pinSum/numPinsdef doubleIntegrate(a, b, c, d, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        pinSum += f(x, y)
    average = pinSum/numPins
    return average*(b - a)*(d - c)

def f(x, y):
    return 4 - x**2 - y**2

##print doubleIntegrate(0, 1.25, 0, 1.25, f, 100000)
    return average*(b - a)*(d - c)

def f(x, y):
    return 4 - x**2 - y**2

##print doubleIntegrate(0, 1.25, 0, 1.25, f, 100000)