'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

'''
walkthrough the problem 
1. O(0)- space complexity
2. O(n)- time complexity
we can sort array in place 
'''


def missing_int(A):
    ''''
    Step 1 - Get +ve max from array - takes O(n)
    step 2 - check if element exist from 1 to max
    '''

    max_ = get_max(A)

    for i in range(1, max_ + 2):
        if i not in A:
            return i


def get_max(A):
    # no inbuilt sort  is used , required TC  is O(n)
    max_ = 0
    for i in range(0, len(A)):
        if A[i] > 0 and A[i] > max_:
            max_ = A[i]
    return max_


print(missing_int([1, 2, 3, 4, 5, 6, 7, -1, -3, -4]))
