from LogEmployee import LogEmployee
from LogRealEstate import LogRealEstate
from LogContractor import LogContractor
from LogMaintenance import LogMaintenance
from LogTicket import LogTicket
from Exceptions import *


import LogEmployee

class DataAPI:
    def __init__(self) -> None:
        self.log_employee = LogEmployee()

    def authenticate_employee_username(self, username: str):
        try:
            return self.log_employee.authenticate_username(username)
        except DataNotFoundException:
            return False

    def get_employees_all(self):
        try:
            return self.log_employee.get_all()
        except DataNotFoundException:
            return False

    def get_employee(self, id_: str):
        try:
            return self.log_employee.get(id_)
        except DataNotFoundException:
            return False

    def post_employee(self, data: str):
        try:
            return self.log_employee.post(data)
        except IncorrectDataException:
            return False

    def put_employee(self, data: str):
        try:
            return self.log_employee.put(data)
        except IncorrectDataException:
            return False
