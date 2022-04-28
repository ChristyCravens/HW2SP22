from math import cos

# Create the secant function to call into the main function
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """The purpose of this function is to use the Secant Method to find the root of the callback fcn(x),
    in the neighborhood of x0 and x1. This function will use the equation to solve for the functions used
    in the main function. "I" serves as a way to keep track of the number of iterations so the loop does
    not exceed the number designated as the max iterations (maxiter).

    :param fcn: this is the callback function for which we want to find the root
    :param x0: this is the newest value in the neighborhood of the root
    :param x1: this is the previous value in the neighborhood of the root
    :param xtol: this tells the computer to exit the loop if |Xnewest - Xprevious|<xtol
    :param maxiter: this tells the computer to exit the loop if the number of iterations reaches this value
    :param return: returns the value of the final estimate of the root (newest x value)

    """

    # Create the starting point of the iterations for the loop, so it begins at 1 instead of 0
    I=0

    # Use a while loop to attain the values of |x0-x1|<xtol with the iterations(I)<=maxiter
    while abs(x0-x1)>=xtol and I<=maxiter:
        # Create the equation for the Secant Method
        x2=x1-(fcn(x1)*(x1-x0))/(fcn(x1)-fcn(x0))
        x0=x1
        x1=x2
        # Tell the computer to add to the values of iterations(I) that'll keep count so it doesn't exceed maxiter
        I+=1
        return x2

# Create the main function to use the previously defined Secant function
def main():

    # Print the first function solution with the parameters for x0, x1, maxiter, and xtol
    F1=lambda x:x-3*cos(x)
    print("Solution of x-3cos(x)=0, with x0=1, x1=2, maxiter=5, and xtol=1e-4: {:0.2f}".format(Secant(F1,1,2,5,1e-4)))

    # Print the second function solution with the parameters for x0, x1, maxiter, and xtol
    F2=lambda x:cos(2*x)*x**3
    print("Solution of cos(2x)*x^3=0, with x0=1, x1=2, maxiter=15, and xtol=1e-8: {:0.2f}".format(Secant(F2,1,2,15,1e-8)))

    # Print the third function solution with the parameters for x0, x1, maxiter, and xtol
    F3=lambda x:cos(2*x)*x**3
    print("Solution of cos(2x)*x^3=0, with x0=1, x1=2, maxiter=3, and xtol=1e-8: {:0.2f}".format(Secant(F3,1,2,3,1e-8)))

main()
