import functools
lst=[10,20,30,31,32]
                                #10,20:10 if 10>20 else 10
minimumval=functools.reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(minimumval)
# output=10