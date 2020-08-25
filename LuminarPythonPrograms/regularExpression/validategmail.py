# Validate Gmail

from re import *

rule='\w*@gmail.com'

gmail=input("Enter gmail : ")

matcher=fullmatch(rule,gmail)

if(matcher !=None):
    print("Valid gmail id")
else:
    print("Invalid gmail id")