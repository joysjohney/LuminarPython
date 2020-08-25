# find element in list

lst=[1,2,3,4,5,6,7,8,9,10,11,12]
element=int(input("Enter element to search : "))
flag=0
for i in lst:
    if(i==element):
        flag+=1
        break
    else:
        pass
if(flag>0):
    print("Element found")
else:
    print("Element not found")