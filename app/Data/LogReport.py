import json
import jsonschema
from models.Schemas import report_schema
import csv

class LogReport:
    def __init__(self) -> None:
        self.path = "csv-files/Report.csv"
        self.fields = list(report_schema["data"].keys())

    def file_report(self, data : json):
        """
            Data: report schema
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
            jsonschema.validate(instance=jsonData, schema=report_schema)
        except jsonschema.exceptions.ValidationError as err:
            return False
        return True

    def get_all_reports_dict(self) -> dict:
        """
        Used by other functions in this class
        in other languages would be "private"
        :returns Dict of all reports
        """
        ret = {"type": "dict", "data": {}}
        with open(self.path, newline='', encoding='utf-8') as report_file:
            reader = csv.DictReader(report_file)
            for row in reader:
                id = row["id"]
                report_dict = {}
                for key in row:
                    report_dict[key]=row[key]
                ret["data"][id] = report_dict
        return ret

    def get_all_reports(self):
        """
        In order not to return plain dict of data
        returns: json dump of all reports
        """
        report = self.get_all_reports_dict()
        return json.dumps(report)
    
    def get_max_id(self):
        """
        returns maximum ID of reports
        """
        max_id = 0
        report = self.get_all_reports_dict()
        for report in report["data"]:
            max_id = report
        return max_id

if __name__ == "__main__":
    pass