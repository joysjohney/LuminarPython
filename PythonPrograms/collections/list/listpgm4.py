lst=[1,2,3,4]
element=int(input("Enter a element : ")) #6
lst.sort()
#[1,2,3,4]
low=0
upp=len(lst)-1
while(low<=upp):
    data=lst[low]+lst[upp] #lst[0]+lst[4] => 1+4=5


    if(data==element):
        print("pairs",lst[low],",",lst[upp])
        break
    elif(data>element):
        upp=upp-1
    else:
        loe=low+1
