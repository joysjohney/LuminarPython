
class Person:
    def setValues(self, pname, age):
        self.age = age
        self.pname = pname

    def printValues(self):
        print(self.pname)
        print(self.age)


class Bank(Person):
    bname = "SBK"  # static variable

    def __init__(self,acno):

        self.acno = acno
        self.balance = 3000

    def deposit(self, amt):

        self.balance += amt
        print("Yor", self.bname, "has been credited with", amt, "on", datetime.data.today())

    def withdraw(self, amt):
        if (amt > self.balance):
            print("Transaction has benn cancelled errorcode 1101")
        else:
            self.balance.amt
            print("Your", self.bname, "has been debited with", amt, "on", datetime.data.today())

    def balanceEnquiery(self):
        print("Your current available balance =", self.balance)


obj=Bank(1001)
obj.printValues("Ajay",25)
obj.printValues()
obj.withdraw(10000)
obj.balanceEnquiery()
