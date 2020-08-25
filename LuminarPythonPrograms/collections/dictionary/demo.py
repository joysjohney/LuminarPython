student={"roll":21,"name":"tinu","age":25,"cpp":25}
print(student["roll"])

#dictionary iteration

for key in student:
    print(key, ":",student[key])

#updating value in dictionary

student["cpp"]+=25
student["name"]="TINU"

#insert a new data

student["total"]=150

print(student)