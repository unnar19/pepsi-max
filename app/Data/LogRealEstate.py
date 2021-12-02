import json
import jsonschema
from Models.Schemas import real_estate_schema
import csv
import os
from Exceptions import *

class LogRealEstate:
    
    def __init__(self) -> None:
        self.path = "csv-files/RealEstate.csv"
        self.fields = list(real_estate_schema["data"].keys())

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
            jsonschema.validate(instance=jsonData, schema=real_estate_schema)
            return True

        # Raise custom Exception for proper error handling
        except jsonschema.exceptions.ValidationError:
            raise IncorrectDataException

    def get_all_real_estate_dict(self) -> dict:
        """
        Used by other functions in this class
        in other languages would be "private"
        :returns Dict of all real estate
        """
        ret = {"type": "dict", "data": {}}
        with open(self.path, newline='', encoding='utf-8') as real_estate_file:
            reader = csv.DictReader(real_estate_file)
            for row in reader:
                id = row["id"]
                real_estate_dict = {}
                for key in row:
                    real_estate_dict[key]=row[key]
                ret["data"][id] = real_estate_dict
        return ret

    def get_all_real_estate(self):
        """
        In order not to return plain dict of data
        returns: json dump of all real estate
        """
        real_estate = self.get_all_real_estate_dict()
        return json.dumps(real_estate)
    
    def get_max_id(self):
        """
        returns maximum ID of real estates
        """
        max_id = 0
        real_estate = self.get_all_real_estate_dict()
        for real_estate in real_estate["data"]:
            max_id = real_estate
        return max_id

if __name__ == "__main__":
    pass