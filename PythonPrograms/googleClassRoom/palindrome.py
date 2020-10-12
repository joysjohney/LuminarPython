# Write a program in Python to check if a sequence is a Palindrome.

num=int(input("Enter a number : "))
temp=num
rev=0
while(num>0):
    k=num%10
    rev=rev*10+k
    num=num//10
if(temp==rev):
    print("Number is Palindrome")
else:
    print("Not palindrome")