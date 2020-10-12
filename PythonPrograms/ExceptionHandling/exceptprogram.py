num1=int(input("Enter value for num1 : "))
num2=int(input("Enter value for num2 : "))
lst=[1,2,3,4]
try:
    res=num1/num2  #it is an abnormal code or case
    print("Result :",res)
    print("We have database transactions")
    print("File operation")
    print("Process completed successfully")
except Exception as e:
    print(e.args)

try:
    pos = int(input("Enter index position : "))  #it is an abnormal code or case
    print(lst[pos])
except Exception as e:
    print(e.args)