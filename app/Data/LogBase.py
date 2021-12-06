import json
import jsonschema
from Exceptions import *
from Models.Schemas import *
import csv
import os

class LogBase:

    __path_and_schema = {
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
        "destination": {
            "path": "csv-files/Destination.csv",
            "schema": destination_schema,
        },
    }

    def __init__(self, key) -> None:
        # Parse path and schema for key
        log_key_dict = LogBase.__path_and_schema[key]
        self.__key = key
        self.__path = log_key_dict['path']
        self.__schema = log_key_dict['schema']

        # Fields in appropriate schema
        self.__fields = list(self.__schema['data'].keys())
        if not os.path.exists(self.__path):
            with open(self.__path,"w"): pass

    ### CRUD ###

    def get_all(self) -> json:
        """
        Read dict from DB
        Return json
        """

        all_items = self.__get_all_dict()
        return json.dumps(all_items)

    def post(self, data : json) -> json:
        """
        WRITE INTERFACE TO DB
        """

        # Parse load from LL
        ll_load = json.loads(data)

        # If file exists
        if os.path.exists(self.__path):
            # Assign id's manually s.a.t. not break unique constraint
            nextid = self.__get_next_id()
            ll_load["data"]["id"] = nextid

        # Validate data from LL
        if self.__validate_json(ll_load, 'POST'):

            with open(self.__path, 'a+', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.__fields)

                # Write header if DB is empty
                if self.__is_empty():
                    writer.writeheader()

                writer.writerow(dict(ll_load['data']))

            # After POST, UI displays POSTED DATA
            return(json.dumps({"type":True, "data": ll_load["data"]}))

    def put(self, data: json) -> json:
        """
        Deletes csv-file and rewrites it with provided data
        """

        # Parse data from LL
        ll_load = json.loads(data)

        # Validate data from LL
        if self.__validate_json(ll_load, 'PUT'):

            # Delete csv-file
            os.remove(self.__path)

            for key in ll_load['data'].keys():
                self.post(json.dumps({"data":ll_load['data'][key]}))

            # Return status code True, and POSTED DATA
            return(json.dumps({"type":True, "data": ll_load["data"]}))



    ### HELPERS ###

    def __is_empty(self) -> bool:
        """
        Returns true if csv-file is empty
        """

        return os.stat(self.__path).st_size == 0

    def __validate_json(self, ll_load: json, method: str) -> bool:
        """
        Returns true if load from LL matches self.__schema
        """

        # Use imported validation feature
        try:
            jsonschema.validate(instance=ll_load, schema=self.__schema)
            return True

        # Raise custom Exception for proper error handling
        except jsonschema.exceptions.ValidationError:
            raise IncorrectDataException(self.__key, method)

    def __get_all_dict(self) -> dict:
        """
        READ INTERFACE TO DB
        """
        if self.__is_empty():
            raise DatabaseEmptyException(self.__key, 'GET_ALL')
        else:
            ret = {"type": "dict", "data": {}}
            with open(self.__path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    id = row["id"]
                    csv_dict = {}
                    for key in row:
                        csv_dict[key]=row[key]
                    ret["data"][id] = csv_dict
            return ret


    def __get_next_id(self) -> int:
        """
        Returns ID for next row
        """
        max_id = 0
        if not self.__is_empty():     
            items = self.__get_all_dict()
            for item in items["data"]:
                max_id = int(item,10)
        return int(max_id) +1


if __name__ == "__main__":
    pass
