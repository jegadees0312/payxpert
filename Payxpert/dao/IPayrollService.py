
from abc import ABC, abstractmethod
from entity.payroll import Payroll
class IPayrollService(ABC):
    @abstractmethod
    def generate_payroll(self, employee_id: int, start_date: str, end_date: str) -> bool:
        pass

    @abstractmethod
    def get_payroll_by_id(self, payroll_id: int) -> Payroll:
        pass

    @abstractmethod
    def get_payrolls_for_employee(self, employee_id: int) -> list[Payroll]:
        pass

    @abstractmethod
    def get_payrolls_for_period(self, start_date: str, end_date: str) -> list[Payroll]:
        pass
