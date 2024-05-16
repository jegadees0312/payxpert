
from abc import ABC, abstractmethod
from entity.employee import Employee
class IEmployeeService(ABC):
    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def add_employee(self, employee_data):
        pass

    @abstractmethod
    def update_employee(self, employee_data):
        pass

    @abstractmethod
    def remove_employee(self, employee_id):
        pass
