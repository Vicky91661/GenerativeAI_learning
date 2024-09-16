class  test:
    pass
test1 = test()
print(type(test1))


class pwskills:
    def Welcome_msg(self):
        print("welcome to pwskills")
myObje = pwskills()
myObje.Welcome_msg()

# Constructor in python

class pwSkills:
    def __init__(self,student_id,name,phone_number,email):
        self.phone_number = phone_number
        self.email = email
        self.student_id = student_id
        self.name = name
    def return_student_details(self):
        return self.student_id,self.name,self.phone_number,self.email
vicky = pwSkills(1,"vicky",384937,"vicky@gmail.com")
print(vicky.return_student_details())

class pwSkills2:
    def __init__(vicky,student_id,name,phone_number,email):
        vicky.phone_number = phone_number
        vicky.email = email
        vicky.student_id = student_id
        vicky.name = name
    def return_student_details(self):
        return self.student_id,self.name,self.phone_number,self.email
vicky = pwSkills2(1,"vicky",384937,"vicky@gmail.com")
print(vicky.return_student_details())