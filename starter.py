"""
STARTER CODE FOR CREATIVE CODING 6
"""

def head(xs):
    return xs[0]

def tail(xs):
    return xs[1::1]


def flatten(xs):
    newList = []
    for x in xs:
        if isinstance(x, list):
            for y in x:
                newList.append(y)
        else:
            newList.append(x)
    return newList

def cons(a, b):
   return flatten([a,b]) 

#----------------------------------------------------
#YOUR CODE HERE


#Question 1
def fact(x):
    if x == 1:
        return 1

    return x + fact(x - 1)

#Question 2
def count(xs):
    if len(xs) == 1:
        return 1

    return 1 + count(tail(xs))

#Question 3
def sumList(xs):
    if len(xs) == 1:
        return head(xs)
    
    return head(xs) + sumList(tail(xs))

#Question 4
def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    return fib(n - 1) + fib(n - 2)

#Question 5
def take(xs, n):
    if n == 1:
        return head(xs)
    
    return cons(head(xs), take(tail(xs), n - 1))


#Question 6
def drop(xs, n):
    if n == 1:
        xs.pop(0)
        return xs
    
    return drop(tail(xs), n - 1)


#----------------------------------------------------

"""
EXAMPLES
"""

def printNums(x):
    print(x)
    if x <= 1:
        return
    printNums(x - 1)

def printList(xs):
    print(head(xs))

    if len(xs) == 1:
        return

    printList(tail(xs))
