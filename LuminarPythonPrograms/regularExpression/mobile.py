# Validate mobile number

from re import *

rule="/d{10}"

mobno=input("Enter mobile  number : ")

matcher=fullmatch(rule,mobno)

if(matcher !=None):
    print("Valid mobile no")
else:
    print("Invalid mobile no!")