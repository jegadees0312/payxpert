
class Employee:
    def __init__(self, employee_id, first_name, last_name, date_of_birth, gender, email, phone_number, address,
                 position, joining_date, termination_date=None):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__position = position
        self.__joining_date = joining_date
        self.__termination_date = termination_date

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_joining_date(self):
        return self.__joining_date

    def set_joining_date(self, joining_date):
        self.__joining_date = joining_date

    def get_termination_date(self):
        return self.__termination_date

    def set_termination_date(self, termination_date):
        self.__termination_date = termination_date

    def __str__(self):
        return f"Employee ID: {self.__employee_id}\nName: {self.__first_name} {self.__last_name}\nDate of Birth: {self.__date_of_birth}\nGender: {self.__gender}\nEmail: {self.__email}\nPhone Number: {self.__phone_number}\nAddress: {self.__address}\nPosition: {self.__position}\nJoining Date: {self.__joining_date}\nTermination Date: {self.__termination_date }"