'''
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
'''

'''
print -  is a function 
         it is an object that you can call, and it writes the arguments to the console with spaces in between
         
         cons(a,b)(print) --- a b 
         
         print, passed to cons(), is assigned to f, and f(a, b) is exactly the same thing as print(a, b).
         
         more example - 
         def add(first, second):
             return first + second
             
        cons(4,5)(add) --- 9
        
        why ? --- functions are objects and can be passed around like other variables
        
        Resource - https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python
'''


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(f):
    def return_first(a, b):
        return a
    return f(return_first)


def cdr(f):
    def return_last(a, b):
        return b

    return f(return_last)

'''
flow of function - car accepts function and cons return function as f(a,b) 
                   this f(a,b) goes to car where f(return_first) -- is just like a,b passes to return_first 
'''
# car accept f and cons return f
print(car(cons(45, 54)))
print(cdr(cons(45, 54)))
