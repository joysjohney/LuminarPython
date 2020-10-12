lst=[10,11,12,13,14,15,2,3,4]
lst.sort()
print(lst)

low=0
upp=len(lst)-1
ele=int(input("Enter element : "))
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(ele>lst[mid]):
        low=mid+1
    elif(ele<lst[mid]):
        upp=mid-1
    elif(ele==lst[mid]):
        flag=1
        break
if(flag>0):
    print("Element found")
else:
    print("Element not found")