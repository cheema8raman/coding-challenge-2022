'''

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?


'''

'''
Resource - https://divyabiyani.medium.com/daily-coding-problem-february-24th-2020-given-a-list-of-integers-write-a-function-that-89b68076b0fb
'''

'''
I need to know only about the i+1 and i+2 sum information for calculating the max sum of the ith position.
Hence, I came up with the logic of only saving 2 sums at a time, and 
finding the new one and replacing it with the following logic.
'''


def maximum_nonadjacent_sum(a):
    first_sum = 0
    second_sum = 0
    for i in range(len(a) - 1, -1, -1):
        new_sum = max(a[i] + second_sum, first_sum)
        second_sum = first_sum
        first_sum = new_sum
    return first_sum


print(maximum_nonadjacent_sum([2, 4, 6, 2, 5]))
print(maximum_nonadjacent_sum([5, 1, 1, 5]))
