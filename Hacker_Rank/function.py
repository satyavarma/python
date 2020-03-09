def disp():
    global x
    x = 20
    y = 20
    print (x,y)
x = 10
y = 10  
print(x,y)
disp()
print(x,y)
print('\n')

#all optional arguments has to be on the right most side
def hapn(a=1,b=2,c=3):
    print(a,b,c)
hapn(1,2,3)
hapn(1,2)
hapn(1)
hapn()
print('\n')

#all keyword parameters has to be on the right most side
hapn(1,c=3,b=2)
print('\n')

#arbitary arguments
def arbdisp(*a):
    print (a)
arbdisp(1)
arbdisp(1,2,3,4)
arbdisp('satya','varma')
k = [1,2,3] # printed as a single list.
arbdisp(k)
print('\n')

#anonymous functions.

anondisp = lambda x: x%2
print (anondisp(2))

k = [1,2,3,4,5,6]
newk = list(filter(lambda x: (x%2==0), k))
print (newk)

newk = list(map(anondisp, k))
print(newk)
print('\n')

#global is nested
def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main : ", x)
print('\n')

#so nonlocal is there
def outer():
    xx = "local"

    def inner():
        nonlocal xx
        xx = "nonlocal"
        print("inner:",xx)

    inner()
    print("outer:", xx)

outer()
#print('xx in main:',xx)
