import json
import jsonschema
from Exceptions import *
from Models.Schemas import *
import csv
import os

class LogBase:

    path_and_schema = {
        "employee": {
            "path": "csv-files/Employee.csv",
            "schema": employee_schema,
        },
        "real_estate": {
            "path": "csv-files/RealEstate.csv",
            "schema": real_estate_schema,
        },
        "ticket": {
            "path": "csv-files/Ticket.csv",
            "schema": ticket_schema,
        },
        "report": {
            "path": "csv-files/Report.csv",
            "schema": report_schema,
        },
        "contractor": {
            "path": "csv-files/Contractor.csv",
            "schema": contractor_schema,
        },
    }


    def __init__(self, key) -> None:

        # Path to .csv file
        log_key_dict = LogBase.path_and_schema[key]
        self.path = log_key_dict['path']

        # Fields in appropriate schema
        self.fields = list(log_key_dict['schema']['data'].keys())

    ### CRUD ###

    def get_all(self):
        """
        In order not to return plain dict of data
        returns: json dump of all employees
        """
        all_items = self.__get_all_dict()
        return json.dumps(all_items)

    def post(self, data : json):
        """
            Data: schema
            :return bool
        """

        # Parse load from LL
        jsondata = json.loads(data)

        # If file exists
        if os.path.exists(self.path):

            # Assign id's manually s.a.t. not break unique constraint
            nextid = self.__get_next_id()
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

    def put(self, data: str):
        """Deletes csv-file and rewrites it with provided data"""

        # Parse data from LL
        load = json.loads(data)

        # Validate data from LL
        if self.__validate_json(load):

            # Delete csv-file
            os.remove(self.path)

            for key in load['data'].keys():
                self.post(json.dumps({"data":load['data'][key]}))

            # Return status code True, but response data is stored in LL
            return(json.dumps({"type":True, "data": None}))


    ### HELPERS ###

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

    def __get_all_dict(self) -> dict:
        """
        Used by other functions in this class
        in other languages would be "private"
        :returns Dict of all items
        """
        ret = {"type": "dict", "data": {}}
        with open(self.path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                id = row["id"]
                csv_dict = {}
                for key in row:
                    csv_dict[key]=row[key]
                ret["data"][id] = csv_dict
        return ret


    def __get_next_id(self):
        """
        returns next ID for item
        """
        max_id = 0
        items = self.__get_all_dict()
        for item in items["data"]:
            max_id = int(item,10)
        return int(max_id) +1


if __name__ == "__main__":
    pass
