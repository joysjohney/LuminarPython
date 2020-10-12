lst=[1,2,3,4]

def square(num):
    return num*num

#map(function,iterables)
#map(square,lst)

sq=list(map(square,lst))
print(sq)