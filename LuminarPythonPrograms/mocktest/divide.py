# Q3. Divide (10,3) o/p = (quot,rem)(3,1) can't use (/) (%)

num1=int(input("Enter number 1 : ")) #10
num2=int(input("Enter number 2 : ")) #3 10/3 =rem=1 quot=3

quot=0
while(num1>num2): #10>3,7>3,4>3
    num1=num1-num2 #num1=10-3=7,7-3=4,4-3=1
    quot+=1 #quo=1,2,3
print("Reminder :",num1)
print("Quotient :",quot)