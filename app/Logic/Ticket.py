from Logic.Base import Base
from Exceptions import *
from datetime import datetime

import json

class Ticket(Base):
    
    def __init__(self) -> None:
        super().__init__("ticket")

    def get_all(self, data: json) -> json:
        return super().get_all(data)

    def get(self, data: json) -> json:
        return super().get(data)

    def post(self, data: json) -> json:
        return super().post(data)

    def put(self, data: json) -> json:
        return super().put(data)
    
    def delete(self, data: json) -> json:
        return super().delete(data)

    # Ticket specific functions:

    def get_filtered_tickets(self, data: json) -> json:
        #All tickets to filter from
        ui_data = json.loads(data)["data"]
        filters = ui_data["filters"]
        filter_data = ui_data["filter_data"]
        
        if "period" in filters:
            all_tickets = self.__get_tickets_filtered_date(filter_data["start_date"], filter_data["end_date"])
            # pop period dates from filters 
            filters.remove("period")
        else:
            all_tickets = json.loads(self.get_all(data))["data"]
        return_data = all_tickets
        # iterate through all tickets and keep those who match
        for filter in filters:
            for key, val in all_tickets.copy().items():
                value = val[filter]
                # for some reason python interprets the nested dict in data as strings even
                # after json.loads, not sure why but this if works
                if filter in ["closed", "ready", "is_recurring"]:
                    value = self.__str2bool(value)
                if value != filter_data[filter]:
                    del return_data[key]
        return json.dumps({"type": "true", "data": return_data})


    def close_tickets(self, data) -> json:
        """Close tickets, takes in data containing ID of ticket - only boss can close"""
        ui_data = json.loads(data)["data"]
        ticket_id = ui_data["id"]
        # only bosses can close tickets
        if ui_data["role"] != "boss":
            raise UnauthorizedRequestException
        
        

    # Helpter functions

    def __get_tickets_filtered_date(self, start_date : str, end_date : str) -> dict:
        """helper function to filter tickets by period"""
        #get all tickets to filter from
        all_tickets = json.loads(self.get_all(json.dumps({"key":"ticket", "data":{}})))
        return_data = {}
        #define start and end as datetime objects
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        #iterate through all tickets
        for key,val in all_tickets["data"].items():
            date = datetime.strptime(val["start_date"], '%Y-%m-%d')
            if start <= date and date <= end:
                return_data[key] = val
        return return_data


    def __str2bool(self, boolean_string: str) -> bool:
        """helper function to turn strings of "true" "True" etc to booleans"""
        return boolean_string.lower() in ("yes", "true", "1", "t")