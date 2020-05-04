# PACKAGE
# Here are the imports again, just in case you need them.
# There is no need to edit or submit this cell.
import numpy as np
import numpy.linalg as la
from readonly.PageRankFunctions import *
np.set_printoptions(suppress=True)

# GRADED FUNCTION
# Complete this function to provide the PageRank for an arbitrarily sized internet.
# I.e. the principal eigenvector of the damped system, using the power iteration method.
# (Normalisation doesn't matter here)
# The functions inputs are the linkMatrix, and d the damping parameter - as defined in this worksheet.
# (The damping parameter, d, will be set by the function - no need to set this yourself.)
def pageRank(linkMatrix, d):
    n = linkMatrix.shape[0] # finds the number of rows in linkMatrix
    
    # set up our initial vector,  r(0), so that we have our 100 Procrastinating Pats 
    # equally distributed on each of our n websites.
    r = 100 * np.ones(n) / n # Sets up this vector for n websites (n entries of 1/n × 100 each)
    
    # This is the matrix that determines where the Pat's visit each minute.
    # It considers the damping factor.
    M = d * linkMatrix + (1-d)/n * np.ones([n, n]) # np.ones() is the J matrix, with ones for each entry.
    
    # automaticaly update the vector after each minute, with the matrix  L
    lastR = r
    r = M @ r
    i = 0
    # sets up a loop so that L keeps being applied to r
    # so that r converges to the correct value
    # until we get within the required tolerance
    while la.norm(lastR - r) > 0.01 :
        lastR = r
        r = M @ r # applies matrix L to r
        i += 1
    
    return r

'''optional:
print(str(i) + " iterations to convergence.")
r'''


