from functools import reduce           #reduce function importing from funtools
def f1(x,y):
    return x+y

def f2(x,y):
    return x-y

def f3(x,y):
    return x*y
l_list=[1,2,3,4,5]
add=reduce(f1,l_list)
sub=reduce(f2,l_list)
mul=reduce(f3,l_list)
print("add",add)
print("sub",sub)
print("mul",mul)

x1=reduce(lambda x,y:x+y,l_list)     #lambda function
print("addition",x1)