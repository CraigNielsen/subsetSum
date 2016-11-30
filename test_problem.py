from functools import reduce
import pytest
import numpy as np
from math import ceil
import pdb

al =[18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
y = 101000000

def sumList(llist):
    return reduce(lambda x,y: x+y, llist)
def test_sumList():
    assert sumList([2,4,6,8]) == 20

def subsetSum(array, total):
    #create array with numbers of array down left and total in columns ie : [len(array) + 1][total + 1]
    #set all row i col 0 to be T
    #iterate through the rest of the rows, and columns
    B = np.zeros((len(array)+1, total+1), dtype=bool)
    B[:, 0]=True
    for i in range(1, len(array) + 1):
        for j in range(1, total + 1):
            if (j - array[i-1] >= 0):
                B[i][j] = B[i-1][j] or B[i-1][j - array[ i - 1]]
            else:
                B[i][j] = B[i-1][j]

    return B[len(array)][total]

def test_SubsetSum():
    assert subsetSum([2,3,7,8,10], 11) == True
    sum_all = sumList(al)
    print(sum_all)
   # assert subsetSum(al, y) == True
