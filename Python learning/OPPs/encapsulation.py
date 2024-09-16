class car:
    def __init__(self,year,make,model,speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed
    def set_speed(self,speed):
        self.__speed = 0 if speed<0 else speed
    def get_speed(self):
        return self.__speed
c = car(2021,"toyota","inova",12)
c.set_speed(34)
print(c.get_speed())



class back_account:
    def __init__(self,balance):
        self.__balance = balance
    def deposite(self,amount):
        self.__balance = self.__balance + amount if amount>0 else 0
    def withdraw(self,amount):
        if amount>self.__balance:
            return False
        else:
            self.__balance=self.__balance - amount
            return True
    def get_balance(self):
        return self.__balance
    

vicky = back_account(1000)
print("your current balance is : ", vicky.get_balance())
print(vicky.withdraw(100))
print("your current balance is : ",vicky.get_balance())