from Log_employee import Log_employee
from Log_building import Log_building
from Log_contractor import Log_contractor
from Log_maintenance import Log_maintenance
from Log_work_order import Log_work_order


import Log_employee

class Data_wrapper:
    def __init__(self) -> None:
        self.log_employee = Log_employee()

    def authenticate_employee_username(self, username):
        return self.log_employee.authenticate_username(username)

    def get_all_employee_fields(self, fields):
        return self.log_employee.get_all_from_fields(fields)
