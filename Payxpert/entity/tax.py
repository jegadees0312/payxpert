
class Tax:
    def __init__(self, tax_id, employee_id, tax_year, taxable_income, tax_amount):
        self.__tax_id = tax_id
        self.__employee_id = employee_id
        self.__tax_year = tax_year
        self.__taxable_income = taxable_income
        self.__tax_amount = tax_amount

    def get_tax_id(self):
        return self.__tax_id

    def set_tax_id(self, tax_id):
        self.__tax_id = tax_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_tax_year(self):
        return self.__tax_year

    def set_tax_year(self, tax_year):
        self.__tax_year = tax_year

    def get_taxable_income(self):
        return self.__taxable_income

    def set_taxable_income(self, taxable_income):
        self.__taxable_income = taxable_income

    def get_tax_amount(self):
        return self.__tax_amount

    def set_tax_amount(self, tax_amount):
        self.__tax_amount = tax_amount

    def __str__(self):
        return f"Tax Details:\n" \
               f"Tax ID: {self.__tax_id}\n" \
               f"Employee ID: {self.__employee_id}\n" \
               f"Tax Year: {self.__tax_id}\n" \
               f"Taxable Income: {self.__taxable_income}\n" \
               f"Tax Amount: {self.__tax_id}\n"