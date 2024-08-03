def f1(num):
    fact=1
    while num!=0:
        fact=fact*num        
        num=num-1
    print(fact)
n1=int(input("enter number"))
f1(n1)