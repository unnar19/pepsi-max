import json
import jsonschema
from models.Schemas import employee_schema
import csv


class Log_employee:

    def __init__(self) -> None:
        self.path = "csv-files/Employee.csv" #spurning ad hafa thetta ekki hardcoded herna?
        self.fields = list(employee_schema["data"].keys())

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
                writer.writerow(dict(jsondata['data']))
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

    def getAllEmployeesDict(self) -> dict:
        """
        Used by other functions in this class
        in other languages would be "private"
        :returns Dict of all employees
        """
        ret = {"type": "dict", "data": {}}
        with open(self.path, newline='', encoding='utf-8') as empfile:
            reader = csv.DictReader(empfile)
            for row in reader:
                id = row["id"]
                emp_dict = {}
                for key in row:
                    emp_dict[key]=row[key]
                ret["data"][id] = emp_dict
        return ret

    def getAllEmployees(self):
        """
        In order not to return plain dict of data
        returns: json dump of all employees
        """
        employees = self.getAllEmployees()
        return json.dumps(employees)

    def authenticateEmp(self, data):
        """
        returns: json object with bool plus emp Data
        """
        data = json.loads(data)
        employees = self.getAllEmployeesDict()
        try:
            employee = employees["data"][str(data["id"])]
        except KeyError:
            return "Employee doesnt exist"
        if str(employee["password"]) == str(data["password"]):
            return json.dumps({"type":True, "data": employee})
        else:
            return json.dumps({"type":False})

    def getMaxId(self):
        """
        returns maximum ID of employees
        """
        max_id = 0
        employees = self.getAllEmployeesDict()
        for employee in employees["data"]:
            max_id = employee
        return max_id


if __name__ == "__main__":
    pass
