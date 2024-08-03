def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
x1=int(input("enter a number"))
print("factorial ::",factorial(x1))