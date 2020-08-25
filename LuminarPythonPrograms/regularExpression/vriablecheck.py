# Rule (20/08/2020)
# ====
# 1) First character is an alphabet and it should be with in a-k
# 2) Second number should be a digit and it must e divisible by 3 =>(3,6,9)
# 3) And the any number of character

from re import *

rule='[a-k][369][a-zA-Z0-9]*'

varname=input("Enter variable name : ")

matcher=fullmatch(rule,varname)

if(matcher !=None):
    print("Valid")
else:
    print("Invalid!")


