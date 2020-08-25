even=[]
odd=[]
sum=0
f=open("numbers", "r")
for num in f:
    if(int(num)%2==0):
        even.append(int(num.rstrip("\n")))
    else:
        odd.append(int(num.rstrip("\n")))
print("Even numbers : ",even)
print("Odd numbers : ",odd)