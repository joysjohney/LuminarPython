from re import *

#pattern="\s" #it will check for spaces

#pattern="\d" #it will check for digit

#pattern="\D" #[^0-9] except digit

#pattern="\w" #check for all words

pattern="\W" #check for all special characters

matcher=finditer(pattern,"abx 7Z#xy@")
for match in matcher:
    print(match.start())
    print(match.group())