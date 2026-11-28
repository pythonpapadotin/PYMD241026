# Classes and objects
# functions ~ methods in oop
# self -> object reference
# implicit passing of arguments: self is implicit passed
# dunder method: double underscore
# dunder method are object methods which are invoked magically or in a
# special manner
# __init__, __str__, __len__,  etc But only __init__ is widely used.

from datetime import datetime


class StudentRegistrationForm:
    def __init__(self, first_name, last_name, date_of_birth, gender):
        self.first_name_mango = first_name
        self.last_name_mango = last_name
        self.date_of_birth_mango = datetime.fromisoformat(date_of_birth)
        self.gender_mango = gender

    def get_full_name(self):
        return self.first_name_mango + " " + self.last_name_mango

    def get_current_age(self):
        current_time = datetime.now()
        age = current_time.year - self.date_of_birth_mango.year
        return age

    def get_basic_info(self):
        age = self.get_current_age()
        full_name = self.get_full_name()
        return f"Name = {full_name}, Age = {age}"

    def __str__(self):
        return f"StudentRegistrationForm of {self.get_full_name()}"


rohan_reg_form = StudentRegistrationForm("Rohan",
                                         "Rathore",
                                         "2010-01-01",
                                         "Male")
# An object will be created in memory and the location/reference will
# be assigned to this variable rohan_reg_form

shyali_reg_form = StudentRegistrationForm("Shyali",
                                         "Singh",
                                         "2013-01-01",
                                         "Female")

# print(rohan_reg_form.get_basic_info())
#
# print(shyali_reg_form.get_basic_info())


print(rohan_reg_form)
