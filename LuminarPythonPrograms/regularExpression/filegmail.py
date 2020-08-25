from re import *
f=open("gmaildata","r")
lst=[]
for line in f:
     data=line.rstrip("\n")
     rule = '\w+[@]\w+[.]\w{2,3}'
     matcher=fullmatch(rule,data)
     if(matcher !=None):
        lst.append(data)
     else:
         pass
print("Valid Gmail ID's :-",lst)