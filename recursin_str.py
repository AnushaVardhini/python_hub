def f1(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+f1(s[:-1])
s2=input("enter a string")
print("reverse::", f1(s2))