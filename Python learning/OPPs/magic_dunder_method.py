print(dir(int))

a= 200
print(a.__add__(5))

class student:
    def __new__(cls):
        pass
    def __init__(self):
        print("this is init ")
        self.mobile_number = 78978534

studentDetails = student()
print(studentDetails.mobile_number)