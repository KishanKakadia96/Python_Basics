# Syntax and Example
# lambda p1, p2: expression

adder = lambda x, y: x + y
print (adder (1, 2))

# What a lambda returns
string='some kind of a lambda function'
print(lambda string : print(string))
# <function <lambda> at 0x00000181F748D2D0>

#What a lambda returns
x="some kind of a useless lambda function"
(lambda x : print(x))(x)

#REGULAR FUNCTION
def func( funct, *args ):
    funct( *args )
def printer_one( arg ):
    return print (arg)
def printer_two( arg ):
    print(arg)
#CALL A REGULAR FUNCTION 
func( printer_one, 'printer 1 REGULAR CALL' )
func( printer_two, 'printer 2 REGULAR CALL \n' )
#CALL A REGULAR FUNCTION THRU A LAMBDA
func(lambda: printer_one('printer 1 LAMBDA CALL'))
func(lambda: printer_two('printer 2 LAMBDA CALL'))

# lambdas in filter function
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))

# lambdas in map function
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences) 
print(list(filtered_result))

# lambdas in reduce function
from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)