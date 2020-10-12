employees=[[1001,"arun",15000],
          [1002,"arjun",20000],
          [1003,"vinu",25000],
          [1004,"binu",18000]]

#print employees name who have salary>17000

# for emp in employees:
#     if(emp[2]>17000):
#         print(emp[1])

#print total salary

for emp in employees:
    sum=sum+emp[2]
print(sum)