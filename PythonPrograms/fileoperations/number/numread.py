f=open("numbers", "r")
lst=[]
for num in f:
    lst.append(int(num.rstrip("\n")))
res=sum(lst)
print(res)