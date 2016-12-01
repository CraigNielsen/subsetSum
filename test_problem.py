from functools import reduce
import pytest
import numpy as np
import pdb

dataset =[18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
y = 101000000

def sumList(llist):
    return reduce(lambda x,y: x+y, llist)
def test_sumList():
    assert sumList([2,4,6,8]) == 20

def subsetSum(array, total):
    #create array with numbers of array down left and total in columns ie : [len(array) + 1][total + 1]
    #set all row i col 0 to be T
    #iterate through the rest of the rows, and columns
    B = np.zeros((len(array), total+1), dtype=bool)
    B[:, 0]=True
    for i in range(len(array) ):
        for j in range(1, total+1 ):
            if i==0:
                B[0][j]=False
            elif (j - array[i] >= 0):
                B[i][j] = B[i-1][j] or B[i-1][j - array[ i ]]
            else:
                B[i][j] = B[i-1][j]
            if j==array[i]: B[i][j]=True

#   trace solution
    solution = []
    i = len(array) - 1
    k = total
    while (k>0):
        if i==0:
            solution.append(array[i])
            break
        if not B[i-1][k]:
            solution.append(array[i])
            k -= array[i]
            i -= 1
        else:
            i -= 1

    has_subset = B[len(array)-1][total]
    return has_subset, solution

def test_SubsetSum():
    assert subsetSum([2,3,7,8], 9) == (True, [7,2])
    assert subsetSum([2,3,7,8,10], 11) == (True, [8,3])
    assert subsetSum([2,3,7,8,10], 18) == (True, [8,7,3])
    assert subsetSum([2,3,7,8,10], 15) == (True, [8,7])
    assert subsetSum([2,3,7,8,109], 15) == (True, [8,7])

    sum_all = sumList(dataset[1:])
    ''' minor optimization for this dataset:
        answer must contain 1st or 2cd element of array: the sum of dataset[2:] < required total
        so can run subset sum without the first element, and attempt to find a solution(minus first element from required_total)
        if solution is found, can add dataset[0] to found solution to get set that sums to required total
        if a solution is not found, you can be sure the second element of the array is part of the subset,
        and run the subsetSum() with for required_total - both first and second elements.
        your final subset will include the second element of given array.
    '''
    total = y-dataset[0]
    has_subset, solution = subsetSum(dataset[1:], total)
    if has_subset == True:
        solution.append(dataset[0])
        print("the solution is: ", solution)
    else:
        total = y-dataset[0]-dataset[1]
        has_subset, solution = subsetSum(dataset[2:], total)
        solution.append(dataset[1])
        print("the solution is: ", solution)

    # solution=  [18897109,2134411, 2142508, 2149127, 2226009, 2543482, 2710489, 2812896, 3095213, 3279933, 4224851, 4296250, 4552402, 5564635, 5582170, 5926800, 6371773, 9661105, 12828837]
    print(sumList(solution))
