# Write a program in Python to produce Star triangle.

n=int(input("Enter the row limit : "))
j=2*n-2
for i in range(0,n):
    for k in range(0,j):
        print(end=" ")
    j=j-1
    for k in range(0,i+1):
        print("*",end=" ")
    print("")