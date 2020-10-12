# Q1. ABABCAAA = print the most frequent character from this string?

str=("ABABABCAAA")
print(str)
dict={}

for data in str:
    if data in dict:
        dict[data]+=1
    else:
        dict[data]=1
print(dict)
result=max(dict,key=dict.get)
print("Frequent character =",result)
