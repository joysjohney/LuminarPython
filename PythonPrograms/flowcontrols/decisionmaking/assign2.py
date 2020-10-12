# dob birth age

bdate=int(input("Enter birth date : "))
bmonth=int(input("Enter birth month : "))
byear=int(input("Enter birth year : "))


cdate=int(input("Enter current date : "))
cmonth=int(input("Enter current month : "))
cyear=int(input("Enter current year : "))

age=cyear-byear
if(bmonth>=cmonth):
    age=age-1
if(bmonth==cmonth):
    if(bdate>cdate):
        age=age-1
print("Your age",age,"years old")