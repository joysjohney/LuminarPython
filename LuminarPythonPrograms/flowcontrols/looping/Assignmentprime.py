# print prime numbers b/w 10 to 50

lower = 10
upper = 50

print("Prime numbers b/w", lower, "and", upper)

for num in range(lower,upper+1):
    if(num>1):
       for i in range(2,num):
           if(num%i==0):
               break
       else:
           print(num)

