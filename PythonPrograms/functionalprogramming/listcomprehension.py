lst=[1,2,3,4,5]

#square
square=[(i*i) for i in lst]
print(square)

#pairs 1,2..1,3..
pairs=[(i,j) for i in lst for j in lst]
print(pairs)

#even
even=[i for i in lst if i%2==0]
print(even)

