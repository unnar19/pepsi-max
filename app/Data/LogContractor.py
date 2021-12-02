import json
import jsonschema
from Models.Schemas import contractor_schema
import csv

class LogContractor:
    
    def __init__(self) -> None:
        self.path = "csv-files/Contractor.csv"
        self.fields = list(contractor_schema["data"].keys())

    def file_contractor(self, data : json):
        """
            Data: contractor schema
            :return bool
        """
        jsondata = json.loads(data)
        isvalid = self.validate_json(jsondata)
        if isvalid:
            with open(self.path, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields)
                writer.writerow(dict(jsondata['data']))
        else:
            # TODO: setja propper error
            raise ValueError()

    def validate_json(self, jsonData):
        """
            jsonData: Json object to validate
            :return bool 
        """
        try:
            jsonschema.validate(instance=jsonData, schema=contractor_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def get_all_contractors_dict(self) -> dict:
        """
        Used by other functions in this class
        in other languages would be "private"
        :returns Dict of all contractors
        """
        ret = {"type": "dict", "data": {}}
        with open(self.path, newline='', encoding='utf-8') as contractor_file:
            reader = csv.DictReader(contractor_file)
            for row in reader:
                id = row["id"]
                contractor_dict = {}
                for key in row:
                    contractor_dict[key]=row[key]
                ret["data"][id] = contractor_dict
        return ret

    def get_all_contractors(self):
        """
        In order not to return plain dict of data
        returns: json dump of all contractors
        """
        contractors = self.get_all_contractors_dict()
        return json.dumps(contractors)

    def get_max_id(self):
        """
        returns maximum ID of contractors
        """
        max_id = 0
        contractor = self.get_all_contractors_dict()
        for contractor in contractor["data"]:
            max_id = contractor
        return max_id

if __name__ == "__main__":
    pass