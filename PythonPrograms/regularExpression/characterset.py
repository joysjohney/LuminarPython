from re import *

#pattern='[abc]' #check for either a,b or c

#pattern='[a-z]' #it will check for lowercase a to z characters

#pattern='[A-Z]' #it will check for uppercase A to Z characters

#pattern='[A-z]' #it will check for both uppercase and lowercase A to z characters

#pattern='[^0-9]'

pattern='[^a-zA-Z0-9]'

matcher=finditer(pattern,"abx% 7Z#xy@")
for match in matcher:
    print(match.start())
    print(match.group())