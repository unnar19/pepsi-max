import json
import Contractor
import Employee
import RealEstate
import Report
import Ticket
from Exceptions import *

# Logic_wrapper is a gateway between UI and Logic classes.
# All UI classes can use the Logic wrapper but only a few
# methods are exposed. Hence, the logic wrapper controls
# all communication between UI and Logic


class LogicAPI:
    def __init__(self) -> None:
        self.employee = Employee()
        self.real_estate = RealEstate()
        self.ticket = Ticket()
        self.contractor = Contractor()

    ### EMPLOYEE METHODS

    def authenticate_employee(self, credentials: str):
        """Credentials contain username-field and password-field"""
        try:
            return self.employee.authenticate(credentials)
        except IncorrectCredentialsException:
            return False

    def get_employees_all(self):
        return self.employee.get_all()

    def get_employee_data(self, id_: str):
        return self.employee.get(id_)

    def post_employee_data(self, data: str):
        try:
            return self.employee.create_new(data)
        except UnauthorizedReguestException:
            return False

    def put_employee_data(self, data: str):
        try:
            return self.employee.update(data)
        except UnauthorizedReguestException:
            return False

    ### REAL ESTATE METHODS

    def get_real_estates_all(self):
        return self.real_estate.get_all()

    def get_real_estate_data(self, id_: str):
        return self.real_estate.get(id_)
    
    def post_real_estate_data(self, data: str):
        try:
            return self.real_estate.post(data)
        except UnauthorizedReguestException:
            return False

    def put_real_estate_data(self, data: str):
        try:
            return self.real_estate.put(data)
        except UnauthorizedReguestException:
            return False

    ### TICKET METHODS

    def get_tickets_all(self):
        return self.ticket.get_all()

    def get_ticket_data(self, id_: str):
        return self.ticket.get(id_)
    
    def post_ticket_data(self, data: str):
        try:
            return self.ticket.post(data)
        except UnauthorizedReguestException:
            return False

    def put_ticket_data(self, data: str):
        try:
            return self.ticket.put(data)
        except UnauthorizedReguestException:
            return False

    ### CONTRACTOR METHODS

    def get_contractors_all(self):
        return self.contractor.get_all()

    def get_contractor_data(self, id_: str):
        return self.contractor.get(id_)

    def post_contractor_data(self, data: str):
        try:
            return self.contractor.post(data)
        except UnauthorizedReguestException:
            return False

    def put_contractor_data(self, data: str):
        try:
            return self.contractor.put(data)
        except UnauthorizedReguestException:
            return False

    