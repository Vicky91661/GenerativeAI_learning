import abc
class pwskills:
    @abc.abstractmethod
    def student_details(self):
        pass

    @abc.abstractmethod
    def student_assignment(self):
        pass

    @abc.abstractmethod
    def student_marks(self):
        pass

class student_details(pwskills):
    def student_details(self):
        return "this is method for taking students details"
    def student_assignment(self):
        return "ths is the method for taking assignment for a particular students"

class data_science_maters(pwskills):
    def student_details(self):
        return "this will return the details of students for data science student"
    def student_assignment(self):
        return "this will return you yhe assignment details for data science student"
