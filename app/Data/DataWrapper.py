from LogEmployee import LogEmployee
from LogRealEstate import LogRealEstate
from LogContractor import LogContractor
from LogMaintenance import LogMaintenance
from LogTicket import LogTicket


import LogEmployee

class DataWrapper:
    def __init__(self) -> None:
        self.log_employee = LogEmployee()

    def authenticate_employee_username(self, username):
        return self.log_employee.authenticate_username(username)

    def get_all_employee_fields(self, fields):
        return self.log_employee.get_all_from_fields(fields)
