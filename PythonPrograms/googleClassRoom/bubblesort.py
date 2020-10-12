# Write a program in Python to execute the Bubble sort algorithm.

lst=[]
num=int(input("Enter the limit : "))
print("Enter values : ")
for k in range(num):
    lst.append(int(input()))
print("Unsorted list : ",lst)

for j in range(len(lst)-1,0,-1):
    for i in range(j):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
print("Sorted list : ",lst)


