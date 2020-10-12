from re import *
f=open("regno","r")
lst=[]
for line in f:
     data=line.rstrip("\n")
     rule = '[Kk][Ll][0-9]{2}[a-zA-Z]{1,2}[0-9]{4}'
     matcher=fullmatch(rule,data)
     if(matcher !=None):
        lst.append(data)
     else:
         pass
print("Valid registration numbers :-",lst)