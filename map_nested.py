p_age=(lambda age:"child" if age<10 else("middle" if age<40 else"senior"))
x1=int(input("enter age"))
print(p_age(x1))                                       