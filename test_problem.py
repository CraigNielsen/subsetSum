from functools import reduce
import numpy as np

dataset = [18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250,
           4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
required_total = 101000000

''' minor optimization for this dataset:
        (1) answer must contain 1st or 2cd element of array because: the sum of dataset[2:] < required total
        so can run subset sum without the first element, and attempt to find a solution (required_total = required_total - first element)
        if solution is found, can add dataset[0] to found subset solution to get the set that sums to the required total

        - if a solution set is not found, you can be sure the second element of the array is part of the subset, (due to (1))
        can run the subsetSum() with: (required_total - both first and second) elements.
        add second element to final subset solution.
    '''


def sum_of_list(llist):
    return reduce(lambda x, y: x + y, llist)


def test_sum_of_list():
    assert sum_of_list([2, 4, 6, 8]) == 20


def subsetSum(array, total):
    # generate grid
    B = np.zeros((len(array), total + 1), dtype=bool)
    B[:, 0] = True
    for i in range(len(array)):
        for j in range(1, total + 1):
            if i == 0:
                B[0][j] = False
            elif (j - array[i] >= 0):
                B[i][j] = B[i - 1][j] or B[i - 1][j - array[i]]
            else:
                B[i][j] = B[i - 1][j]
            if j == array[i]:
                B[i][j] = True

#   trace solution
    solution = []
    i = len(array) - 1
    k = total
    while (k > 0):
        if i == 0:
            solution.append(array[i])
            break
        if not B[i - 1][k]:
            solution.append(array[i])
            k -= array[i]
            i -= 1
        else:
            i -= 1

    has_subset = B[len(array) - 1][total]
    return has_subset, solution


def test_SubsetSum():
    assert subsetSum([2, 3, 7, 8], 9) == (True, [7, 2])
    assert subsetSum([2, 3, 7, 8, 10], 11) == (True, [8, 3])
    assert subsetSum([2, 3, 7, 8, 10], 18) == (True, [8, 7, 3])
    assert subsetSum([2, 3, 7, 8, 10], 15) == (True, [8, 7])
    assert subsetSum([2, 3, 7, 8, 109], 15) == (True, [8, 7])

    total = required_total - dataset[0]
    has_subset, solution = subsetSum(dataset[1:], total)
    if has_subset:
        solution.append(dataset[0])
        print("the solution is: ", solution)
    else:
        total = required_total - dataset[0] - dataset[1]
        has_subset, solution = subsetSum(dataset[2:], total)
        solution.append(dataset[1])
        print("the solution is: ", solution)

    # solution=  [18897109, 2134411, 2142508, 2149127, 2226009, 2543482, 2710489, 2812896, 3095213, 3279933, 4224851, 4296250, 4552402, 5564635, 5582170, 5926800, 6371773, 9661105, 12828837]
    assert sum_of_list(solution) == required_total
    print("final solution sum: ", sum_of_list(solution))
