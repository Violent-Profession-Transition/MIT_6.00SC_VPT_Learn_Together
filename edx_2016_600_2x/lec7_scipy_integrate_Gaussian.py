import scipy.integrate, pylab


def gaussian_distri(x, mu, sigma):
    """the probability density function of
    Gaussian distribution
    in PDF, only the AUC matters"""
    factor1 = 1.0 / (sigma * ((2 * pylab.pi)**0.5))
    factor2 = pylab.e**-(((x-mu)**2) / (2 * sigma**2))
    return factor1*factor2

def integrate_gaussian(numStd, mu, sigma):
    """use scipy.integrate.quad to integrate
    Gaussian distribution PDF"""
    area = scipy.integrate.quad(
               gaussian_distri,
               mu - numStd*sigma,
               mu + numStd*sigma,
               (mu, sigma)
           )
    return area
