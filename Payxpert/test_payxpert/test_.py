import pytest
from dao.impl import PayrollService, EmployeeService, TaxService
from entity.employee import Employee
@pytest.fixture
def payrolls():
    return PayrollService()

def test_getpayrollbyid(payrolls):
    result=payrolls.get_payroll_by_id(2)
    assert result != False

def test_getpayrollforemployee(payrolls):
    result=payrolls.get_payrolls_for_employee(6)
    assert result != False

@pytest.fixture

def employee():
    return EmployeeService()
def test_addemployee(employee):
    object=Employee( employee_id=100, first_name="Test", last_name="test1", date_of_birth="2000-12-12", gender="male", email="gfyteugghjkg@yjtgu", phone_number="7623482364", address="iury uyrytr iury",
                 position="Developer", joining_date="2023-12-12", termination_date="2023-12-30")
    result= employee.add_employee(object)
    assert result == True

def test_deleteemployee(employee):
    result= employee.remove_employee(100 )
    assert result == True



