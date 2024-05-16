
from abc import ABC, abstractmethod
from entity.FinancialRecord import FinancialRecord
class IFinancialRecordService(ABC):
    @abstractmethod
    def add_financial_record(self, record_id,employee_id: int,date, description: str, amount: float, record_type: str) -> bool:
        pass

    @abstractmethod
    def get_financial_record_by_id(self, record_id: int) -> FinancialRecord:
        pass

    @abstractmethod
    def get_financial_records_for_employee(self, employee_id: int) -> list[FinancialRecord]:
        pass

    @abstractmethod
    def get_financial_records_for_date(self, record_date: str) -> list[FinancialRecord]:
        pass
