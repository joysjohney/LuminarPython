# program to print odd sum and even sum in a range

low=int(input("Enter lower limit : "))
upp=int(input("Enter upper limit : "))
evensum=0
oddsum=0
for i in range(low,(upp+1)):
    if(i%2==0):
        evensum=evensum=i
    else:
        oddsum=oddsum+i
print(oddsum)
print(evensum)