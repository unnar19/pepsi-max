import json
import jsonschema
from Models.Schemas import employee_schema
from Exceptions import *
import csv

class LogEmployee:

    def __init__(self) -> None:
        self.path = "csv-files/Employee.csv" #spurning ad hafa thetta ekki hardcoded herna?
        self.fields = list(employee_schema["data"].keys())

    def post(self, data : json):
        """
            Data: employee schema
            :return bool
        """
        jsondata = json.loads(data)
        print(jsondata)
        isvalid = self.validate_json(jsondata)
        if isvalid:
            with open(self.path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields)
                print(self.fields)
                writer.writerow(dict(jsondata['data']))
        else:
            # TODO: setja propper error
            # TODO: return-a status code fyrir UI -Eyþór
            raise ValueError()

    def validate_json(self, jsonData):
        """
            jsonData: Json object to validate
            :return bool 
        """
        try:
            jsonschema.validate(instance=jsonData, schema=employee_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def get_all_employees_dict(self) -> dict:
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

    def get_all(self):
        """
        In order not to return plain dict of data
        returns: json dump of all employees
        """
        employees = self.get_all_employees_dict()
        return json.dumps(employees)

    def get_password(self, data):
        """
        returns: json object with bool plus emp Data
        """
        data = json.loads(data)
        employees = self.get_all_employees_dict()
        try:
            employee = employees["data"][str(data["id"])]
        except KeyError:
            return json.dumps({"type":False, "data": ""})
        return json.dumps({"type":True, "data": employee})
       

    def get_max_id(self):
        """
        returns maximum ID of employees
        """
        max_id = 0
        employees = self.get_all_employees_dict()
        for employee in employees["data"]:
            max_id = employee
        return max_id


if __name__ == "__main__":
    pass
