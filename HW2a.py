from math import sqrt, exp, pi
# Import the math functions needed throughout these programs: square root, exponential, and pi


def Probability(PDF, args, c, GT=True):
    """
    Uses Simpson's Rule to integrate PDF, returning a probability P(x<c) being False. Passes the PDF to
    the Simpson function for integration.

    :param PDF: this is the callback function for the GNPDF
    :param args: tuple containing mean and standard deviation
    :param c: floating point value for P(x<c)
    :param GT: boolean for P(x>c) as GT=True and P(x<c) as GT=False
    :return: P(x<c) or P(x>c)
    """

    # I need to integrate PDF between x=m-5*s and c, where b=c
    # Identify values for a, b, and nPoints for integration
    a = args[0]-args[1]*5
    b = c
    nPoints = 1000

    # Define the area under the curve by passing PDF along to the Simpson function that will perform the operation.
    area=Simpson(PDF, args, a, b, nPoints)

    # Calculate the probability of x>c or x<c and arrange them accordingly (x>c: 1-area).
    # This says that if GT=True, then it will be the first return, but if false, it'll be the second.
    if GT:
        return 1-area
    else:
        return area




def GNPDF(x, args):
    """
    Uses the Gaussian Normal Probability Density Function, about the population mean (m) and
    the population standard deviation (s).

    :param x: value used in comparison with c for the probability
    :param args: mean, standard deviation
    :return: f(x) as Fn
    """

    # Unpack args first
    m,s = args
    # Create the function (Fn) for the GNPDF and return the resultant
    Fn = (1/(s*sqrt(2*pi))) * exp(-0.5*((x-m)/s)**2)
    return Fn


def Simpson(fcn, args, a, c, nPoints=1000):
    """Uses the Simpson's 1/3 Rule for numerical integration to calculate the area under the curve from a to b

    :param fcn: this is the function to be integrated with Simpson's 1/3 rule
    :param args: tuple containing to pass to fcn
    :param a: lower limit of integration
    :param c: upper limit of integration, also equal to b
    :param nPoints: number of points to calculate the area under the curve
    :return: value of the area under the curve after the integration is performed
    """
    # Redefine a and b, then calculate the value for h
    a = args[0] - args[1]*5
    b = c
    h = (b-a)/nPoints

    # List for the values for x
    x = list()
    # List for the values for f(x)
    fx = list()
    # "I" keeps track of the loop iterations until it reaches nPoints
    I = 0
    # Loop the program until all iterations are completed
    while I <= nPoints:
        x.append(a+I*h)
        fx.append(fcn(x[I], args))
        I += 1

    # Create a list to store resulting values, as well as establishing the iterations counter again
    result = 0
    I = 0
    # Loop to determine resulting values until nPoints is reached, while organizing said values
    while I <= nPoints:
        if I == 0 or I == nPoints:
            result += fx[I]
        elif I % 2 != 0:
            result += 4*fx[I]
        else:
            result += 2*fx[I]
        I += 1
    result = result*(h/3)
    return result



def main():
    """
    This function uses the probability function to find P(x<1|N(0,1)): probability x<1 given a normal
    distribution of x with m=0, s=1 P(x>m+2s|N(173,3))
    :return: print statement of probability
    """

    # Re-pack arguments and define value of c
    args = (0, 1)
    c = args[0]+args[1]
    # Give the solution for P(x<1.00|N(0,1)), rounded to 2 decimals
    P1 = Probability(GNPDF, args, c, GT=False)
    print("Probability of x<1.00 in a normal distribution between (0,1): {:0.2f}%".format(P1*100))

    # Give the solution for P(x>181.00|N(175,3)), rounded to 2 decimals
    args = (175, 3)
    c = args[0] + 2*args[1]
    P2 = Probability(GNPDF, args, c, GT=True)
    print("Probability of x>181.00 in a normal distribution between (175,3): {:0.2f}%".format(P2*100))



main()
