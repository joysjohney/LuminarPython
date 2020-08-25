import re

#pattern="a+" #it will check for occurances for a

#pattern="a*"

#pattern="a?"

pattern="a{2}"


matcher = re.finditer(pattern,"aabaaaabaaaabaabbababbaa#$^&*")
count = 0
for match in matcher:
    print(match.start())
    print(match.group())
    count += 1
print(count)