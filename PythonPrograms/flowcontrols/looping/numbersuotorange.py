# program to print numbers upto a range

low=int(input("Enter low limit : "))
limit=int(input("Enter limit : "))
while(low<=limit):
    if(low%2==0):
        print(low)
    low+=1