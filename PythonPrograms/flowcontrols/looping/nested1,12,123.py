#1
#12
#123

for i in range(1,4): #i=1 i=2 i=3
    for j in range(1,i+1): #j(1,2) j(1,2,3) j(1,4)
        print(j,end="") #1 12 123
    print()