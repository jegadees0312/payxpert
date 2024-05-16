import mysql.connector

from util.db_conn_util import DBConnUtil
from exceptions.custom_exceptions import EmployeeNotFoundException, PayrollGenerationException, TaxCalculationException, \
    FinancialRecordException, InvalidInputException, DatabaseConnectionException
from entity.employee import Employee
from entity.FinancialRecord import FinancialRecord
from entity.tax import Tax
from entity.payroll import Payroll
from dao.IPayrollService import IPayrollService
from dao.IEmployeeService import IEmployeeService
from dao.IFinancialRecordService import IFinancialRecordService
from dao.ITaxService import ITaxService

class EmployeeService(IEmployeeService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def get_employee_by_id(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeID = %s", (employee_id,))
            employee_data = cursor.fetchone()
            cursor.close()

            if employee_data:
                return Employee(*employee_data)
            else:
                return False
        except mysql.connector.Error as e:
            print("Error :",e)


    def get_all_employees(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Employee")
            employees_data = cursor.fetchall()
            cursor.close()


            employees =[Employee(*data) for data in employees_data]
            return employees

        except mysql.connector.Error as e:
            print("Error :",e)

    def add_employee(self, employee_data):
        try:
            cursor = self.connection.cursor()
            insert_query = ("INSERT INTO Employee (EmployeeId,FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)")
            values = (employee_data.get_employee_id(),
                employee_data.get_first_name(), employee_data.get_last_name(), employee_data.get_date_of_birth(), employee_data.get_gender(),
                employee_data.get_email(), employee_data.get_phone_number(), employee_data.get_address(), employee_data.get_position(),
                employee_data.get_joining_date(), employee_data.get_termination_date())
            cursor.execute(insert_query, values)
            self.connection.commit()
            cursor.close()
            #self.connection.close()

            return True
        except Exception as e:
            raise DatabaseConnectionException("Error adding employee to database: " + str(e))

    def update_employee(self, employee_data):
        try:
            if not employee_data:
                raise InvalidInputException("Employee data is empty")

            cursor = self.connection.cursor()
            update_query = "UPDATE Employee SET EmployeeId=%s, FirstName=%s, LastName=%s, DateOfBirth=%s, Gender=%s, Email=%s, PhoneNumber=%s, Address=%s, Position=%s, JoiningDate=%s, TerminationDate=%s WHERE EmployeeID=%s"
            values = (employee_data.employee_id,
                employee_data.first_name, employee_data.last_name, employee_data.date_of_birth, employee_data.gender,
                employee_data.email, employee_data.phone_number, employee_data.address, employee_data.position,
                employee_data.joining_date, employee_data.termination_date, employee_data.employee_id)
            cursor.execute(update_query,values)
            self.connection.commit()
            cursor.close()


            return True
        except Exception as e:
            raise DatabaseConnectionException("Error updating employee in database: " + str(e))

    def remove_employee(self, employee_id):
        try:

            cursor = self.connection.cursor()
            sett = "set foreign_key_checks=0"
            cursor.execute(sett)
            delete_query = "DELETE FROM Employee WHERE EmployeeID = %s"
            cursor.execute(delete_query, (employee_id,))
            self.connection.commit()
            cursor.close()

            return True
        except mysql.connector.Error as e:
            print("Error :",e)

class PayrollService(IPayrollService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()
        super()

    def generate_payroll(self, employee_id, start_date, end_date):
        try:
            cursor = self.connection.cursor()
            payroll_data = cursor.execute(f"select * from (select * from payroll where employeeid={employee_id})as subquery where '{start_date}' >= payperiodstartdate and '{end_date}' <= payperiodenddate")
            payroll_data=cursor.fetchone()
            cursor.close()


            if payroll_data:
                return Payroll(*payroll_data)
            else:
                return False
        except mysql.connector.Error as e:
            self.connection.close()
            self.connection=DBConnUtil.get_connection()
            print("Error :",e)

    def get_payroll_by_id(self, payroll_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE PayrollID = %s", (payroll_id,))
            payroll_data = cursor.fetchone()
            cursor.close()
            #self.connection.close()

            if payroll_data:
                return Payroll(*payroll_data)
            else:
                return False
        except mysql.connector.Error as e:
            print("Error :",e)

    def get_payrolls_for_employee(self, employee_id):
        try:

            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE EmployeeID = %s", (employee_id,))
            payrolls_data = cursor.fetchall()
            cursor.close()


            payrolls = []
            for payroll_data in payrolls_data:
                payrolls.append(Payroll(*payroll_data))
            if payrolls:
                return payrolls
            else:
                return False
        except mysql.connector.Error as e:
            print("Error :",e)

    def get_payrolls_for_period(self, start_date, end_date):
        try:

            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Payroll WHERE PayPeriodStartDate >= %s AND PayPeriodEndDate <= %s", (start_date, end_date))
            payrolls_data = cursor.fetchall()
            cursor.close()


            payrolls = []
            for payroll_data in payrolls_data:
                payrolls.append(Payroll(*payroll_data))
            if payrolls:
                return payrolls
            else:
                return False
        except mysql.connector.Error as e:
            print("Error :",e)

    def calculate_gross_salary(self, employee_id):
        return employee_id.salary
class TaxService(ITaxService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def calculate_tax(self, employee_id, tax_year):
        try:
            cursor = self.connection.cursor()

            tax_data = cursor.execute(f"SELECT * FROM Tax WHERE EmployeeID = {employee_id} AND TaxYear ={tax_year}")
            tax_data=cursor.fetchone()
            cursor.close()

            if tax_data:
                return Tax(*tax_data)
            else:
                return False
        except mysql.connector.Error as e:
            self.connection.close()
            self.connection = DBConnUtil.get_connection()
            print("Error :",e)

    def get_tax_by_id(self, tax_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Tax WHERE TaxID = %s", (tax_id,))
            tax_data = cursor.fetchone()
            cursor.close()
            #self.connection.close()

            if tax_data:
                return Tax(*tax_data)
            else:
                return False
        except mysql.connector.Error as e:
            print("Error :",e)

    def get_taxes_for_employee(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Tax WHERE EmployeeID = %s", (employee_id,))
            taxes_data = cursor.fetchall()
            cursor.close()
            #self.connection.close()

            taxes = []
            for tax_data in taxes_data:
                taxes.append(Tax(*tax_data))

            return taxes
        except mysql.connector.Error as e:
            print("Error :",e)

    def get_taxes_for_year(self, tax_year):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Tax WHERE TaxYear = %s", (tax_year,))
            taxes_data = cursor.fetchall()
            cursor.close()

            taxes = []
            for tax_data in taxes_data:
                taxes.append(Tax(*tax_data))
            if taxes:
                return taxes
            else:
                return False
        except mysql.connector.Error as e:
            print("Error :",e)

    def calculate_net_salary(self, employee):
        tax_amount = employee.salary * 0.1
        net_salary = employee.salary - tax_amount
        return net_salary


class FinancialRecordService(IFinancialRecordService):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def add_financial_record(self, record_id,employee_id, description, amount, record_type):
        try:
            if not description or not amount or not record_type:
                raise InvalidInputException("Invalid input data for adding financial record")

            cursor = self.connection.cursor()
            insert_query = "INSERT INTO FinancialRecord (RecordId,EmployeeID, Description, Amount, RecordType) VALUES (%s, %s, %s, %s,%s)"
            cursor.execute(insert_query, (record_id,employee_id, description, amount, record_type))
            self.connection.commit()
            cursor.close()


            return True
        except mysql.connector.Error as e:
            print("Error :",e)

    def get_financial_record_by_id(self, record_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE RecordID = %s", (record_id,))
            financial_record_data = cursor.fetchone()
            cursor.close()

            if financial_record_data:
                return FinancialRecord(*financial_record_data)

            else:
                return False
        except mysql.connector.Error as e:
            print("Error :",e)

    def get_financial_records_for_employee(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE EmployeeID = %s", (employee_id,))
            financial_records_data = cursor.fetchall()
            cursor.close()
            #self.connection.close()

            financial_records = []
            for financial_record_data in financial_records_data:
                financial_records.append(FinancialRecord(*financial_record_data))

            return financial_records
        except Exception as e:
            raise DatabaseConnectionException("Error retrieving financial records from database: " + str(e))

    def get_financial_records_for_date(self, record_date):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM FinancialRecord WHERE RecordDate = %s", (record_date,))
            financial_records_data = cursor.fetchall()
            cursor.close()
            #self.connection.close()

            financial_records = []
            for financial_record_data in financial_records_data:
                financial_records.append(FinancialRecord(*financial_record_data))

            return financial_records
        except Exception as e:
            raise DatabaseConnectionException("Error retrieving financial records from database: " + str(e))
