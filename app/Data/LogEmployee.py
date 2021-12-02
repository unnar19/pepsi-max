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
        isvalid = self.validate_json(jsondata)
        # set ID manually til að: not break unique contraint
        nextid = self.get_next_id()
        jsondata["data"]["id"] = nextid
        if isvalid:
            with open(self.path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields)
                writer.writerow(dict(jsondata['data']))
            return(json.dumps({"type":True, "data": jsondata["data"]}))
        else:
            # TODO: setja propper error
            return(json.dumps({"type":False, "data": "Invalid schema"}))

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


    def get_employee_by_id(self, id : int) -> json:
        """
        parameters: json {"id":id}
        returns: json {"id":id, "data":{(all employee data with id)}
        """
        employees = self.get_all_employees_dict()
        return json.dumps(employees["data"][id])


    def get_next_id(self):
        """
        returns next ID for employees
        """
        max_id = 0
        employees = self.get_all_employees_dict()
        for employee in employees["data"]:
            max_id = int(employee,10)
        return int(max_id) +1

    def update_employee_tickets(self):
        pass


if __name__ == "__main__":
    pass
