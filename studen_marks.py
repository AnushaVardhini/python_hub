'''p_marks=(lambda marks:"Fail" if marks<35 else("C grade" if marks<40 else("B grade" if marks<60 else "A grade")))
x1=int(input("enter marks"))
print(p_marks(x1))'''



p_marks=(lambda marks:"Fail" if marks<35 else("C grade" if marks<40 else("B grade" if marks<60 else "A grade")))
print(p_marks(20)) 
print(p_marks(50)) 
print(p_marks(60)) 
print(p_marks(45)) 