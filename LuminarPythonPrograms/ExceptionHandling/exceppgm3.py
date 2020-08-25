num1=int(input("Enter value for num1 : "))
num2=int(input("Enter value for num2 : "))

try:
    res=num1/num2  #it is an abnormal code or case
    print("Result :", res)
except Exception as e:
    num1=int(input("Enter value for num1 : "))
    num2=int(input("Enter value for num2 : "))
    try:
        res=num1/num2  #it is an abnormal code or case
        print("Result",res)
    except Exception as e:
        print(e.args)
finally:
    print("We have database transactions")
    print("File operation")
    print("Process completed successfully")