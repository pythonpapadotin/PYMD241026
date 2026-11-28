from datetime import datetime


class StudentRegistrationForm:
    total_no_of_students = 0  # class attribute

    def __init__(self, first_name, last_name, date_of_birth, gender):
        self.first_name_mango = first_name
        self.last_name_mango = last_name
        self.date_of_birth_mango = datetime.fromisoformat(date_of_birth)
        self.gender_mango = gender
        StudentRegistrationForm.total_no_of_students += 1

    def get_full_name(self):
        return self.first_name_mango + " " + self.last_name_mango

    @classmethod
    def get_total_number_of_students(cls):
        return cls.total_no_of_students

    @staticmethod
    def get_name_of_school():
        return "APS Delhi"


print("Total Students = ",
      StudentRegistrationForm.get_total_number_of_students())

rohan_reg_form = StudentRegistrationForm("Rohan",
                                         "Rathore",
                                         "2010-01-01",
                                         "Male")

shyali_reg_form = StudentRegistrationForm("Shyali",
                                         "Singh",
                                         "2013-01-01",
                                         "Female")

print("Total Students = ",
      StudentRegistrationForm.get_total_number_of_students())

print(shyali_reg_form.get_name_of_school())
