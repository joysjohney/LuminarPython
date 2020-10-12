# Q5. [1,2,3,4] (6)

lst=[1,2,3,4]
ele=int(input("Enter element : "))
lst.sort()
low=0
upp=len(lst)-1

while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==ele):
        print("Pairs :",lst[low],",",lst[upp])
        break
    elif(data>ele):
        upp=upp-1
    else:
        low=low+1
print()