
class FinancialRecord:
    def __init__(self, record_id, employee_id, record_date, description, amount, record_type):
        self.__record_id = record_id
        self.__employee_id = employee_id
        self.__record_date = record_date
        self.__description = description
        self.__amount = amount
        self.__record_type = record_type

    def get_record_id(self):
        return self.__record_id

    def set_record_id(self, record_id):
        self.__record_id = record_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_record_date(self):
        return self.__record_date

    def set_record_date(self, record_date):
        self.__record_date = record_date

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_record_type(self):
        return self.__record_type
        
    def set_record_type(self, record_type):
        self.__record_type = record_type

    def __str__(self):
        return f"Financial Record Details:\n" \
               f"Record ID: {self.__record_id}\n" \
               f"Employee ID: {self.__employee_id}\n" \
               f"Record Date: {self.__record_date}\n" \
               f"Description: {self.__description}\n" \
               f"Amount: {self.__amount}\n" \
               f"Record Type: {self.__record_type}\n"


