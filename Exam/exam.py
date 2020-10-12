# fetchdata(state="kerala") total number of confirmed cases
# fetchdata(satate="kerala",param="recoverd")
# fetchdata(state="kerala",param="death")


f=open("complete.csv","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirmed=data[4]
    recovered=data[6]
    death=data[5]
    if (state not in dict):
        dict[state] = {"confirmed": confirmed, "recovered": recovered, "death": death}
    else:
        dict[state] = {"confirmed": confirmed, "recovered": recovered, "death": death}

def Fetchdata(**kwargs):
    if(kwargs["state"] not in dict):
        print("State does not found")
    else:
        for k,v in dict.items():
            if(k==kwargs["state"]):
                print("Total number of confirmed cases :",v["confirmed"])
                if("param" in kwargs):
                    val=kwargs["param"]
                    if(val=="recovered"):
                        print("Recoverd :",v["recovered"])
                    elif(val=="death"):
                        print("Total number of death :",v["death"])

Fetchdata(state="Kerala",param="death")
