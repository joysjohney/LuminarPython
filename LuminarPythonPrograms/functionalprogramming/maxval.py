import functools
lst=[10,20,30,31,32]
                                #32,31:32 if 32>31 else 30
maxval=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(maxval)
# output=32