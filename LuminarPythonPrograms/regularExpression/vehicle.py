# Validate all vehicle registration number


from re import *

rule='[Kk][Ll] [0-9]{2} [a-zA-Z]{1,2} \d{4}'

regno=input("Enter Vehicle reg number : ")

matcher=fullmatch(rule,regno)

if(matcher !=None):
    print("Valid Reg no")
else:
    print("Invalid Reg no!")