#Function One - Sum array
def sum_array(array):

    '''Return sum of all items in array'''
    if len(array)==1:
        return array[0]
    else:
        return array[0] + sum_array(array[1:])

#Function Two - Find nth fibonacci number
def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n < 0:
        print('Invalid input, try again')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        nth = fibonacci(n - 1) + fibonacci(n - 2)
        return nth

#Function Three - find n!
def factorial(n):

    '''Return n!'''
    if n < 0:
        print('No Factorial For Negative Number')
    elif (n == 0) or (n == 1):
        return 1
    else:
        return n * factorial(n - 1)

#Function Four - reverse word
def reverse(word):

    '''Return word in reverse'''
    rev_word = ""
    for i in word:
        rev_word = i + rev_word
    return rev_word
