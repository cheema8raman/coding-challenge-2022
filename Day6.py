'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

'''

'''
walkthrough -- count single digit first 
               two at a time
               ignore last case if last element is 0 
               
Resource referred - https://blog.devgenius.io/daily-coding-problem-problem-7-d2dc3bbf7c30
                
'''


def recursion(data: str, k: int) -> int:
    # If the length is zero, we have reached the end of the string. Since it is empty, we return 1
    if k == 0:
        return 1
    s = len(data) - k
    res = recursion(data, k - 1)
    # To check if two digits before k are within the permissible range, k must be atleast. Hence we add
    # the condition 'k >= 2' and check the number 'data[s:s+2]' is within [0,26].
    if k >= 2 and (data[s]+data[s + 1]) < 27:
        res += recursion(data, k - 2)
    return res


def count(message):
    if message.startswith('0') or len(message) == 0:
        return 'Not allowed'

    elements = [int(i) for i in message]

    if elements[-1]==0:
        return recursion(elements, len(elements)) -1
    else:
        return recursion(elements, len(elements))


print(count('120')) # [12,20] , [1,20]
print(count('111')) # [1,1,1] , [11,1] , [1,11]
