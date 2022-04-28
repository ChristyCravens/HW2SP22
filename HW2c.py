import numpy as np
# Import a math function that explicitly is beneficial to linear algebra and matrices. This function being imported,
# "numpy," allows for ease of manipulation of matrices values, without having to write the code for it more thoroughly
# in each change to the matrix. It allows for use of function such as the determinant values. However, I did have
# trouble importing only the pieces I wanted, so I used the shortcut "np" to call the function when needed.

def Cramer(Aaug):
    """
    This function uses Cramer's method to solve a system of linear equations in a matrix by replacing one column of
    A values within the matrix with b values for D1, then the second column in the matrix is replaced with b values
    for D2. The function then returns the vector containing the solution.
    :param Aaug: this is the augmented matrix [A|b], having N rows and N+1 columns, with N representing the number
    of equations
    :return x: this is the vector containing the solution
    """
    # Cramer's function says that if Ax=b and D=|A|, then D1=[b1, a12; b2, a22] and D2=[a11, b1; a21, b2]. Then
    # you can determine if there is a solution, no solution, or infinite solutions based on whether or not D=0
    # and the values of the altered matrices. If det(D) does not =0, the solutions exists, so you can solve for it.
    # If det(Di)/=0, the solution doesn't exist. If det(Di)=0 there are infinite solutions.

    # Create dictionaries to store all values of the matrices. D=|A| and Di=D1, D2
    D = Aaug[:,:-1]
    b = Aaug[:,-1]
    Di = []
    solution = []

    # Find the new version of D where b replaces the first column, then the second, & append the dictionary D1
    # with the new found values.
    for i in range(len(Aaug[:,0])):
        Di.append(np.delete(np.insert(D,i,b,axis=1),i+1,axis=1))

    # If det(D)/=0, there is a solution.
    if np.linalg.det(D) != 0:
        # Divide det(Di) by Det(D), then append the dictionary solution with the results
        for i in range(len(Di)):
            x = np.linalg.det(Di[i])/np.linalg.det(D)
            solution = np.append(solution,x)
    # If det(D)=0, check if the det(Di)=0
    else:
        # If det(Di)/=0, there is no solution.
        for i in range(len(Di)):
            if np.linalg.det(Di[i]) != 0:
                solution = np.array([np.nan])
            print("There is no solution to this equation.")

        # If det(Di)=0, there are infinite solutions.
        else:
            x = np.linalg.det(Di[i]) / np.linalg.det(D)
            solution = np.append(solution, x)
            print("There are an infinite number of solutions.")

    # Print the solution after the if/else statements have organized the appropriate result/values, depending.
    return solution





def main():

    # Define the matrices to be used in the program when the Cramer function is called.
    A0=np.array([[3,1,-1,2], [1,4,1,12], [2,1,2,10]])
    A1=np.array([[1,-10,2,4,2], [3,1,4,12,12], [9,2,3,4,21], [-1,2,7,3,37]])

    # Print the solutions using the Cramer method of the above matrices.
    print("The solution for matrix A0 is: ", Cramer(A0))
    print("The solution for matrix A1 is: ", Cramer(A1))

main()