class studentDetails:
    def student_details(self,name,email_id,number):
        print(name,email_id,number)

    @staticmethod
    def mentor_mail_id(mail_id_mentor):
        print(mail_id_mentor)
    
    @staticmethod
    def mentor_class(list_mentor):
        studentDetails.mentor_class(["vicky@gmail.com","ritik@gmial.com"])

    @classmethod
    def class_name(cls):
        cls.mentor_class(["vicky","ritik"])
    
    def mentor(self,mentor_list):
        print(mentor_list)
        self.mentor_class(["vicky","ritik"])