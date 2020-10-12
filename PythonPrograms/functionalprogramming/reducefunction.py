import functools
lst=[10,20,30,31,32]

total=functools.reduce(lambda num1,num2:num1+num2,lst)
                                # 10,20:10+20=30
                                # 30,30:30+30=60
                                # 60,31:60+31=91
                                # 91,32:91+32=123
print(total)
# output=123