'''
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
'''
from operator import add as plus

one = [[1, -2], [-3, 4]]
two = [[2, -1], [0, -1]]
three = [[3, -3], [2, -2]]

# def add(matrix1, matrix2):
# 	answer = [list(map(plus, x[0], x[1])) for x in zip(matrix1, matrix2)]
# 	return answer

# add(one, two)

# For the first bonus, modify your add function to accept and "add" any number of lists-of-lists. 

def add(*args):
	print(args)
	answer = list(zip(args))
	print(answer)
	return answer

add(one, two, three)

