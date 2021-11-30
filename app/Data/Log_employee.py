import json
import jsonschema
from models.Schemas import employee_schema
import csv


class Log_employee:

    def __init__(self) -> None:
        self.path = "csv-files/Employee.csv" #spurning ad hafa thetta ekki hardcoded herna?
        self.fields = list(employee_schema["properties"].keys())

    def create_new_employee(self, data : json):
        """
            Data: employee schema
            :return bool
        """
        jsondata = json.loads(data)
        isvalid = self.validateJson(jsondata)
        if isvalid:
            with open(self.path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields)
                writer.writerow(dict(jsondata['properties']))
        else:
            # TODO: setja propper error
            raise ValueError()

    def validateJson(self, jsonData):
        """
            jsonData: Json object to validate
            :return bool 
        """
        try:
            jsonschema.validate(instance=jsonData, schema=employee_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def getAllEmployees(self):
        

    def authenticateEmp(self, data):
        pass

if __name__ == "__main__":
    employeeshit = Log_employee()
    data = {"type":"dict",
            "data": {
                "name":"einar",
                "username": "einsi",
                "password": "12345",
                "ssn":15555555,
                "address": "einarville",
                "home_phone": 3333,
                "mobile_phone": 333333,
                "email": "Einar@kingsi.is",
                "location": "whoville"
        }}
    testshit = json.dumps(data, indent = 4)
    employeeshit.create_new_employee(testshit)
