# print 2nd largest number

num1=int(input("Enter for num1 : ")) #60
num2=int(input("Enter for num2 : ")) #55
num3=int(input("Enter for num3 : ")) #50

if((num1>num2)&(num1>num3)): #(60>55)&(60<50)
    if(num2>num3): #55>50
        print("num2 max",num2)
    else:
        print("second largest number is", num2)
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print("second largest number is",num1)
    else:
        print("second largest number is",num3)
elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print("second largest number is",num1)
    else:
        print("second largest number is",num2)
else:
    print("numbers are equal")
