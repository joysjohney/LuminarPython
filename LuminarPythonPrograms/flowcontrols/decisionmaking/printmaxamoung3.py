# print maximum number amoung 3 number

num1=int(input("Enter num1 : ")) #10
num2=int(input("Enter num2 : ")) #20
num3=int(input("Enter num3 : ")) #30
if((num1>num2)&(num1>num3)):
    print("max=",num1) #(10>20)&(10>30)
elif((num2>num1)&(num2>num3)):
    print("max=",num2) #(20>10)&(20>30)
elif((num3>num1)&(num3>num2)):
    print("max=",num3)
else:
    print("numbers are equal")