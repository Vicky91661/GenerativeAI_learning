class studentDetails:
    mobile_number = 9166
    def __init__(self,name,email,number) -> None:
        self.name = name
        self.email = email
        self.mobile_number = number
    def print_details(self):
        print("Name of student is "+self.name+" and email is "+self.email+" and phone number is ", self.mobile_number)
    @classmethod
    def putdetails(cls ,name, email,number):
        return cls(name,email,number)
studentOne = studentDetails("vicky","vicky@gmail.com",167568)
print("the mobile number for student one is ",studentOne.mobile_number)
studentOne.mobile_number = 788937
print("the mobile number for student one is ",studentOne.mobile_number)
studentOne.print_details()

studentTwo = studentDetails.putdetails("ritik","ritik@gmail.com",70231)
print("the mobile number for student two is ",studentTwo.mobile_number)
studentTwo.print_details()