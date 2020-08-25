f=open("covid_19_india.csv","r")
dict={}
dict2={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    confirmed=data[8]
    if state not in dict and state not in dict2:
        dict[state]=death
        dict2[state]=confirmed
    else:
        dict[state]=death
        dict2[state]=confirmed
totaldeath=0
totalconfirmed=0
dlst=[]
clst=[]
for k,v in dict.items():
    dlst.append(int(v))
    totaldeath+=int(v)
    print(k,v)
for k,v in dict.items():
    if(max(dlst)==int(v)):
        print("\nState with highest death cases      :",k,"-",v)

for k,v in dict2.items():
    clst.append(int(v))
    totalconfirmed+=int(v)
for k,v in dict2.items():
    if(max(clst)==int(v)):
        print("State with highest confirmed cases  :",k,"-",v)

print("Total confirmed cases in india      :",totalconfirmed)
print("Total death in India                :",totaldeath)



