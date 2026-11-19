"""Lab 05 portfolio submission template (Exercise 1 code).

Submit this file, plus a separate .md or .txt file with your written
explanation, to Gradescope. Fill in the TODOs below - do not rename either
function, the autograder looks up `generate_table` by name.

What you need to do:
  1. Implement `gram_schmidt_qr`: the classical Gram-Schmidt QR
     factorisation, as covered in the lectures.
  2. Implement `generate_table`: build the eps/error1/error2/error3 table
     for eps = 10**-6, ..., 10**-16 using `gram_schmidt_qr`, and save it to
     "table.csv" in the working directory - the autograder looks for that
     exact filename, with a header row and columns named exactly
     eps, error1, error2, error3.
"""

import numpy as np


def A_func(eps):
    return np.array([[1, 1 + eps], [1 + eps, 1]], dtype=float)


def gram_schmidt_qr(A):
    """
    Compute the QR factorisation of a square matrix using the classical
    Gram-Schmidt process.

    Parameters
    ----------
    A : numpy.ndarray
        A square 2D NumPy array of shape ``(n, n)`` representing the input
        matrix.

    Returns
    -------
    Q : numpy.ndarray
        Orthonormal matrix of shape ``(n, n)`` where the columns form an
        orthonormal basis for the column space of A.
    R : numpy.ndarray
        Upper triangular matrix of shape ``(n, n)``.
    """
    n, m = A.shape
    if n != m:
        raise ValueError(f"the matrix A is not square, {A.shape=}")

    Q = np.empty_like(A)
    R = np.zeros_like(A)

    # TODO: fill in Q and R

    for j in range (n):
        v = A[:, j].copy()
        for i in range(j):
            R[i, j]=np.dot(Q[:, j], A[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)As 
        Q[:, j] = v / R[j, j]

    '''
    Im including a long winded explanation as i worked through this as it was quite complicated
    For the TODO section of this function I started off with a loop using j as my value that is going to loop n times (the number of columns in A). So I am looping through the columns in short. 
By using j (which automatically starts at 0) I make a copy of the matrix column so as not to edit the original matrix (also just made it easier to access), which then allows me to carry on with my algorithm.
As n is 2 (meaning j will do 0 then 1), on the first pass of the first for loop, the inner loop does not run, which is perfect because the first column for Gram Schmidt's factorisation does not need projecting.

So for the first column, the algorithm will go straight to normalising as it does not need projecting. 
Right now, V = A's first column so I use the built in function to calculate the length it and store it in R[j, j] which, at this point in time, is the top left corner of R.
For Q, I then divide the v (the first column of A at this point in time) by the length that I calculated for R [j, j] and store that number in both rows of the first column of Q. Q now stores in its first column the normalised values. 

My first loop now repeats with n being the second column of A so j = 1. 
I then copy the second column of A into v.
As j is now 1, my inner loop can computer for the first time. 
I = 0 at this point in time also.
This part of the loop then calculates the projection coefficient by doing the dot product of the first column that's just been stored in Q and the second column of A, which is stored in the top right of R.
This has also allowed for the calculation of the perpendicular, by subtracting the projection from v(which is still the second column in A) and overwrites v to be the perpendicular. 
The inner loop has now finished. As of right now, R has its top row filled in, and Q as the first column filled in. 

The final two lines of the loop are then executed, with j = 1 this time. the length is calculated for our new v and stored in the bottom right of R. 
This means that R is now complete, with our values in the upper triangle.
We finally normalise for Q but this time for Q's second column and using R[1, 1].
Q is now complete. 
    '''

    return Q, R


def generate_table():
    """
    Build the eps/error1/error2/error3 table for eps = 10**-6, ..., 10**-16
    using gram_schmidt_qr, and save it to "table.csv" (the autograder looks
    for this exact filename).
    """
    # TODO: build the table and save it, e.g.
    import pandas as pd

    rows = []
    for eps in [10**-j for j in range(6, 17)]:
        A = A_func(eps)
        Q, R = gram_schmidt_qr(A)
        
        error1 = np.linalg.norm(A - Q @ R)
        error2 = np.linalg.norm(Q.T @ Q - np.eye(A.shape[0]))
        error3 = np.linalg.norm(R - np.triu(R))

        rows.append(
            {"eps": eps, "error1": error1, "error2": error2, "error3": error3}
        )
    pd.DataFrame(rows).to_csv("table.csv", index=False)


if __name__ == "__main__":
    generate_table()
