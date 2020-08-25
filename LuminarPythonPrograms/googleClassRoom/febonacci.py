# Write a program to produce Fibonacci series in Python.

num=int(input("Enter the limit : "))
num1=0
num2=1
temp=0
for i in range(num):
    print(num1,end="")
    temp=num1
    num1=num2
    num2=temp+num2
