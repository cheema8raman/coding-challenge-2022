'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

# Way 1
def is_sum_to(a, k):

    '''
    :param a: list or array
    :param k: int
    :return: True if sum ==k exists else False
    '''

    ''' Method 1 
    for i in range(0,len(a)-1):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                return True
    return False
    '''
    #Method  2
    subtraction_set = set()
    for i in range(0, len(a)):
        subtraction_set.add(k - a[i])
    if a[i] in subtraction_set:
        return True

    return False

print(is_sum_to([10,15,3,7],k=17))

