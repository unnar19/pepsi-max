import json
import jsonschema
from Models.Schemas import destination_schema
import csv

class LogDestination:
    
    def __init__(self) -> None:
        self.path = "csv-files/Destination.csv"
        self.fields = list(destination_schema["data"].keys())

    def file_destination(self, data : json):
        """
            Data: destination schema
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
        else:
            # TODO: setja propper error
            raise ValueError()

    def validate_json(self, jsonData):
        """
            jsonData: Json object to validate
            :return bool 
        """
        try:
            jsonschema.validate(instance=jsonData, schema=destination_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def get_all_destinations_dict(self) -> dict:
        """
        Used by other functions in this class
        in other languages would be "private"
        :returns Dict of all destinations
        """
        ret = {"type": "dict", "data": {}}
        with open(self.path, newline='', encoding='utf-8') as destination_file:
            reader = csv.DictReader(destination_file)
            for row in reader:
                id = row["id"]
                destination_dict = {}
                for key in row:
                    destination_dict[key]=row[key]
                ret["data"][id] = destination_dict
        return ret

    def get_all_destinations(self):
        """
        In order not to return plain dict of data
        returns: json dump of all destinations
        """
        destinations = self.get_all_destinations_dict()
        return json.dumps(destinations)

    def get_destination_by_id(self, id : int) -> json:
        """
        parameters: json {"id":id}
        returns: json {"id":id, "data":{(all destination data with id)}
        """
        destinations = self.get_all_destinations_dict()
        return json.dumps(destinations["data"][id])

    def get_next_id(self):
        """
        returns next ID for destinations
        """
        max_id = 0
        destinations = self.get_all_destinations_dict()
        for destinations in destinations["data"]:
            max_id = int(destinations,10)
        return int(max_id) +1

if __name__ == "__main__":
    pass