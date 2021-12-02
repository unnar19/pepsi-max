import json
import jsonschema
from Models.Schemas import real_estate_schema
import csv

class LogRealEstate:
    
    def __init__(self) -> None:
        self.path = "csv-files/RealEstate.csv"
        self.fields = list(real_estate_schema["data"].keys())

    def file_real_estate(self, data : json):
        """
            Data: real estate schema
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
            jsonschema.validate(instance=jsonData, schema=real_estate_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

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