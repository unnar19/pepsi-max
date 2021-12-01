import json
import jsonschema
from models.Schemas import ticket_schema
import csv

class LogTicket:
    def __init__(self) -> None:
        self.path = "csv-files/Ticket.csv"
        self.fields = list(ticket_schema["data"].keys())

    def file_ticket(self, data : json):
        """
            Data: ticket schema
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
            jsonschema.validate(instance=jsonData, schema=ticket_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def get_all_tickets_dict(self) -> dict:
        """
        Used by other functions in this class
        in other languages would be "private"
        :returns Dict of all tickets
        """
        ret = {"type": "dict", "data": {}}
        with open(self.path, newline='', encoding='utf-8') as ticket_file:
            reader = csv.DictReader(ticket_file)
            for row in reader:
                id = row["id"]
                ticket_dict = {}
                for key in row:
                    ticket_dict[key]=row[key]
                ret["data"][id] = ticket_dict
        return ret

    def get_all_tickets(self):
        """
        In order not to return plain dict of data
        returns: json dump of all tickets
        """
        ticket = self.get_all_tickets_dict()
        return json.dumps(ticket)
    
    def get_max_id(self):
        """
        returns maximum ID of reports
        """
        max_id = 0
        ticket = self.get_all_tickets_dict()
        for ticket in ticket["data"]:
            max_id = ticket
        return max_id

if __name__ == "__main__":
    pass