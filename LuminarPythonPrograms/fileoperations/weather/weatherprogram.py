f=open("temeraturedata", "r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    district=data[0]
    temperature=data[1]
    print(district)
    print(temperature)
    if(district not in dict):
        dict[district]=temperature
    else:
        old=dict[district]
        if temperature>old:
            dict[district]=temperature

print(dict)