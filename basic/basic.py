#!/usr/bin/python3
# the above command is used to convert the file into executable.
'''multiline 
comment'''
days = '''satya varma
    siva vamsi'''
print (days)
print('\n')

var1 = 235
print(var1)
var1 = 'satya'
print(var1)
print('\n')

a = b= c = 1
print(a,b,c)
d,e,f =2,3,'satya'
print(d,e,f)
# print(10+'sai')
print('\n')

del var1
del a,b,c
# print (var1,a,b,c)
arr1 = [1,2,3,'satya']
del arr1[2]
print (arr1)
print('\n')


stri= 'Hello World!'
print (stri)          # Prints complete string
print (stri[0])       # Prints first character of the string
print (stri[2:5])     # Prints characters starting from 3rd to 5th
print (stri[2:])      # Prints string starting from 3rd character
print (stri * 2)      # Prints string two times
print (stri + "TEST"+'\n') # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
numlist = [1,2]
numlist2 = [ 2,4]
print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (numlist*2)     # print list two times even the elements are numbers only
#print (numlist+2)
print (list + tinylist) # Prints concatenated lists
print (numlist + numlist2)
print (numlist, numlist2)
print ('\n')


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
numtuple = (1,2)
print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (numtuple * 2)    #  ''
#print (numtuple+2)
print (tuple + tinytuple) # Prints concatenated tuple

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list
print ('\n')

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print('\n')

print(11//3)
print(-11//3)
print([1,3] == [1,3], 9 == 9, 'hi' == 'hi')
print([1,3] is [1,3], 9 is 9, 'hi' is 'hi')
print ("\n")

num_int = 123
num_str = '456'
print (type(num_int))
print (type(num_str))
num_int = str(num_int)
print (type(num_int))
print (num_int+num_str)
num = int(num_int)
numm = int(num_str)
print (num+numm)
print ('\n')


print(1,2,3,4,sep='*')
print(numlist, sep=' ', end='\n')
print(numlist)

print('my name is {} with roll-no {}'.format('satya',55))
print('my name is {1} with roll-no {0}'.format(55,'satya'))
print('my name is {name} with roll-no {id}'.format(name='satya',id=55),end='\n')

name = 'satya'
idn = 55
print('my name is %s with roll-no' %name ,'%2.2f' %idn, end='\n')

import sys
print (sys.path)
print ('\n')

print(type(range(1,10)))
a = range(1,10)
print(type(a))
print(a)
print(range(1,10))
for num in a:
    print (num, end=',')
print('\n')
