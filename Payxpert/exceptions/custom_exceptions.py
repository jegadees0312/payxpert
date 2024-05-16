class EmployeeNotFoundException(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

class PayrollGenerationException(Exception):
    def __init__(self, message="Error generating payroll."):
        self.message = message
        super().__init__(self.message)

class TaxCalculationException(Exception):
    def __init__(self, message="Error in tax calculation."):
        self.message = message
        super().__init__(self.message)

class FinancialRecordException(Exception):
    def __init__(self, message="Financial record error."):
        self.message = message
        super().__init__(self.message)

class InvalidInputException(Exception):
    def __init__(self, message="Invalid input data."):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):
    def __init__(self, message="Database connection error."):
        self.message = message
        super().__init__(self.message)
