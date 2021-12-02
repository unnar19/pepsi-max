import json
import jsonschema
from Models.Schemas import employee_schema
from Exceptions import *
import csv
import os

class LogEmployee:

    def __init__(self) -> None:
        self.path = "csv-files/Employee.csv" #spurning ad hafa thetta ekki hardcoded herna?
        self.fields = list(employee_schema["data"].keys())

    def post(self, data : json):
        """
            Data: employee schema
            :return bool
        """

        # Parse load from LL
        jsondata = json.loads(data)

        # If file exists
        if os.path.exists(self.path):

            # Assign id's manually s.a.t. not break unique constraint
            nextid = self.get_next_id()
            jsondata["data"]["id"] = nextid

        # Validate data from LL
        if self.__validate_json(jsondata):

            with open(self.path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields)

                # Write header if DB is empty
                if self.__is_empty():
                    writer.writeheader()

                writer.writerow(dict(jsondata['data']))

            return(json.dumps({"type":True, "data": jsondata["data"]}))


    def __is_empty(self):
        """Returns true if csv-file is empty"""
        return os.stat(self.path).st_size == 0

    def __validate_json(self, jsonData):
        """
            jsonData: Json object to validate
            :return bool 
        """

        # Use imported validation feature
        try:
            jsonschema.validate(instance=jsonData, schema=employee_schema)
            return True

        # Raise custom Exception for proper error handling
        except jsonschema.exceptions.ValidationError:
            raise IncorrectDataException

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

    def put(self, data: str):
        """Deletes csv-file and rewrites it with provided data"""

        # Parse data from LL
        load = json.loads(data)

        # Validate data from LL
        if self.validate_json(load):

            # Delete csv-file
            os.remove(self.path)

            for key in load['data'].keys():
                self.post(json.dumps({"data":load['data'][key]}))

            # Return status code True, but response data is stored in LL
            return(json.dumps({"type":True, "data": None}))

if __name__ == "__main__":
    pass
