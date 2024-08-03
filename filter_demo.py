numbers_=[1,2,3,4,5,6]
even_list=list(filter(lambda num:num%2==0, numbers_))
print("even numbers",even_list)
odd_list=list(filter(lambda num:num%2!=0, numbers_))
print("odd numbers",odd_list)