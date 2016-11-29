from functools import reduce
import pytest
from math import ceil
import pdb

al =[18897109, 12828837, 9661105, 6371773, 5965343, 5926800, 5582170, 5564635, 5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279933, 3095213, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127, 2142508, 2134411]
y = 101000000
    #find mean of a list of numbers
def mean(x):
    return reduce((lambda x,y: x+y), x)/len(x)
    # find closest number to one given in a list
def findClosest(llist, number):
    return reduce((lambda x,current: x if (abs(x-number) < abs(number-current)) else current), llist)
    #remove a given number from a list
def removeFromList(llist, number):
    llist.remove(number)
    return llist
def sumList(llist):
    return reduce(lambda x,y: x+y, llist)
def findFirstMatchingPair(llist, degree):
    pair = []
    for i in range(len(llist)):
        for j in range(1, len(llist[i:]) ):
            if ((llist[i]+llist[i+j])%degree == 0):
                pair.append(llist[i])
                pair.append(llist[i+j])
                return pair
    return []

def test_mean():
    assert mean([100,110,120,130,140]) == 120
def test_findClosest():
    assert (findClosest([2,3,44,49,70], 48))==49
def test_sumList():
    assert sumList([2,4,6,8]) == 20
def test_removeFromList():
    assert removeFromList([2,4,6,8], 6) == [2,4,8]
def test_findFirstMatchingPair():
    assert findFirstMatchingPair([ 1234, 3454, 2327, 2995, 8996, ], 10) == [1234, 8996]
    assert findFirstMatchingPair([ 3452, 2327, 2995, 8996, 1234, ], 10) == [8996, 1234]
    assert findFirstMatchingPair([ 4433, 1234, 2327, 4366, 8996, ], 100) == [1234, 4366]
    assert findFirstMatchingPair([ 4433, 1234, 2324, 4363, 8993, ], 100) == []

def reduce_pairs(llist, degree):
    new_list = []
    leftovers = llist.copy()
    while (True):
        result = []
        result = findFirstMatchingPair(leftovers, degree)
        if result == []:
            break
        else:
            removeFromList(leftovers, result[0])
            removeFromList(leftovers, result[1])
            new_list.append(sumList(result))
    return new_list, leftovers

def iterate_degrees(llist, degree, max_degree, all_leftovers):
    pairs, leftovers = reduce_pairs(llist, degree)
    all_leftovers += leftovers
    new_degree = degree*10
    if len(pairs) == 1:
        return pairs, all_leftovers
    if new_degree > max_degree:
        return pairs, all_leftovers
    else:
        return iterate_degrees(pairs, new_degree, max_degree, all_leftovers)

def test_iterate_degrees():
    assert iterate_degrees([273, 284, 277, 266, 341, 289, 345, 233], 10, 100, []) == ([1100], [345,233,630])

def test_reduce_pairs():
    assert reduce_pairs([1234, 2346, 3333, 7777, 2832,2334], 10) == ([3580, 11110], [2832, 2334])
    assert reduce_pairs([1234, 3333], 10) == ([], [1234, 3333])
    assert reduce_pairs([1234, 3333], 100) == ([], [1234, 3333])
    assert reduce_pairs([1234, 3336], 10) == ([4570], [])

others = []
def zeros_approach():
#create new list
#find pairs,remove from old list and add to new list as sum of pair
#add leftovers to leftovers array
#call again with new list
    full_list = al.copy()
    degree = 10
    while (degree < 10000):
        pairs, leftovers = reduce_pairs(full_list, degree)

        degree = degree*10


#find all matching pairs in 1st degree
#save all others
#find all matching pairs in 2cd degree
#save all others
#iterate until 5th degree
    pass

@pytest.mark.skip()
def test_main():
    print( (sumList(al) - y) )
    print (y/64)
    t = [20,30,40,50,60,70]
    final = 40+60+70
    solved = []
    print('start with mean: ', mean(t))
    number_of_terms = ceil(final/mean(t))
    print('find out number of terms', number_of_terms)
    close = findClosest(t, mean(t))
    solved.append(close)
    print('adding the closest to the remainder :', close)
    t = removeFromList(t, close)
    print('so far solved is: ', solved)
    print('so far t is: ', t)
    print('find number closest to final - sum(solved) / numbers')
    print("________________")
    while (sumList(solved) != final):
        k = t.copy()
        x = 0
        for i in t.copy():
            cl = ( final - sumList(solved) ) / ( number_of_terms - x)
            x+=1
            if cl < min(k):
                print("solved is ", solved)
                print("number of terms too big cl:;", cl)
                solved=[close]
                break
            closest = findClosest(k, cl)
            solved.append(closest)
            k = removeFromList(k, closest)
        print ("finished")
        print(solved, "is final")
        number_of_terms -= 1 #TODO: start again
    print(solved)
    pytest.fail()

    # def popfirstpair(x, running):
        # # pdb.set_trace()
        # if running == 10: return x
        # for i in range((len(x))):
            # if ( (x[i] + running ) % 10 ==0 ):
                # print(x[i])
                # return x[i]
            # else:
                # return popfirstpair(x[1:], running+x[i])

            # for j in range(len(x[i:])):
                # for k in range(len(x[i+j:])):
                    # for l in range(len(x[i+j+k:])):
                        # if ((x[i]+x[i+j]+x[i+j+k]+x[i+j+k+l])%1000 == 0):
                            # a = x[i]
                            # b = x[i+j]
                            # c = x[i+j+k]
                            # d = x[i+j+k+l]
                            # x.pop(i+j+k+l)
                            # x.pop(i+j+k)
                            # x.pop(i+j)
                            # x.pop(i)
                            # return a,b,c,d
    # total = 0
    # y=101000000
    # while (len(x)>4):
        # a,b,c,d = popfirstpair(x)
        # total += a
        # total += b
        # total += c
        # total += d
        # print(total, " ", y-total)
        # print(x)

    # print(mean)
    # findClosest(lis, value):
        # x=
