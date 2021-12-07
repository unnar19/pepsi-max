import json
from Data.DataAPI import DataAPI
from Exceptions import *

class Base:

    __required = {
        "employee":{
            "role", "name", "password", "ssn", "address", \
            "mobile_phone", "email", "destination"
        },
        "real_estate":{
            "real_estate_id", "address", "destination"
        },
        "ticket":{
            "real_estate_id", "description", "destination", "start_date", "employee_id"
        },
        "report":{
            "real_estate_id", "description", "employee_id", "destination", "start_date"
        },
        "contractor":{
            "name", "contact", "phone", "opening_hours", "destination"
        },
        "destination":{
            "airport", "country", "phone", "opening_hours", "manager_id"
        }
    }
    __autofill = {
        "employee":{
            "home_phone": None,
            "tickets": [],
            "reports": []
        },
        "real_estate":{
            "tickets": [],
            "reports": [],
            "maintenance_info": None
        },
        "ticket":{
            "report_id": 0,
            "close_date": "future",
            "priority": False,
            "open": True,
            "is_recurring": False
        },
        "report":{
            "ticket_id": 0,
            "total_price": 0,
            "contractor_id": 0,
            "contractor_pay": 0,
            "close_date": "future",
            "comments": [],
            "ready": False,
            "closed": False
        },
        "contractor":{
            "tickets": []
        },
    }
    __unique = {
        "employee": "email",
        "real_estate": "real_estate_id",
        "contractor":"phone",
        "destination":"airport"
    }

    def __init__(self, key, identifier='id') -> None:
        self.__data_api = DataAPI()
        self._key = key
        self._identifier = identifier

        if key in Base.__unique.keys():
            self._unique = Base.__unique[key]
        else:
            self._unique = None
            
        if key in Base.__required.keys():
            self._required = Base.__required[key]
        else:
            self._required = set()

        if key in Base.__autofill.keys():
            self._autofill = Base.__autofill[key]
        else:
            self._autofill = dict()
        
    ### CRUD ###

    def get_all(self, data: json) -> json:
        # Parse data from UI

        if self.__wants_filter(data):

            ui_load = json.loads(data)
            # Parse filter category and value from UI
            filter_category, filter_value = ui_load['data']['filter'], ui_load['data']['filter_value']

            # Parse all data from DL
            all_data = json.loads(self.__data_api.get_all(data))

            # Collect data that fulfills filters
            filtered_data = {}
            for key, value in all_data["data"].items():
                if value[filter_category] == filter_value:
                    filtered_data[key] = value

            # Construct response
            response = {"type": "dict", "data" :filtered_data}
            return json.dumps(response)
        else:
            return self.__data_api.get_all(data)

    def get(self, data: json) -> json:
        """
        Searches data_load for identifier
        Identifier should be the key for each instance data value
        """
        ui_load = json.loads(data)['data']
        try:
            search_key = ui_load[self._identifier]
        except KeyError:
            search_key = ui_load[self._unique]

        data_load = json.loads(self.get_all(data))['data']
        try:
            return json.dumps({"type": True, "data": data_load[str(search_key)]})
        except KeyError:
            raise NotFoundException(self._key, 'GET')

    def post(self, data: json) -> json:
        if self.__is_boss(data):
            
            if self.__correct_fields(data):
                
                # Some data, e.g. Destination do not have autofill values
                if not self._autofill:
                    pass
                else:
                    data = self.__autofill_input(data)

                # Some data, e.g. Tickets do not have a unique identifier
                if not self._unique:
                    return self.__data_api.post(data)
                elif self.__is_new(data):
                    return self.__data_api.post(data)
                else:
                    raise DataAlreadyExistsException(self._key, 'POST')

            else:
                raise IncorrectFieldsException(self._key, 'POST')
        else:
            raise UnauthorizedRequestException(self._key, 'POST')

    def put(self, data: json) -> json:
        """
        Data argument should only contain data from 1 item

        Put requests must come with an ID
        """

        if self.__is_boss(data):
            
            # Parse user input
            ui_load = json.loads(data)['data']

            # Validate input
            if self.__valid_put_data(ui_load, 'PUT'):

                # Parse DB response
                data_load = json.loads(self.get_all(data))['data']

                # Replace item data
                id_ = ui_load['id']
                for key, val in ui_load.items():
                    data_load[id_][key] = val

                # Send fixed data to DL to be written
                fixed_data = json.dumps({"key": self._key, "data": data_load})
                response = json.loads(self.__data_api.put(fixed_data))

                # Return fixed data to UI to be displayed
                if response['type']:
                    response['data'] = data_load[id_]

                    return json.dumps(response)

        else:
            raise UnauthorizedRequestException(self._key, 'PUT')

    def delete(self, data : json) -> json:
        """
        Deletes entry with id_ in json
        only one entry
        uses put method in datalayer
        """
        if self.__is_boss(data):
            # parse json
            ui_load = json.loads(data)['data']

            if self.__valid_put_data(ui_load, 'DELETE'):
                #get all data
                data_load = json.loads(self.get_all(data))['data']
                
                id_ = ui_load['id']
                try:
                    # delete form data
                    del data_load[str(id_)]
                except KeyError:
                    raise IncorrectIdException(self._key, 'DELETE')

                #make put request with all data exept given load
                fixed_data = json.dumps({"key": self._key, "data": data_load})
                response = json.loads(self.__data_api.put(fixed_data))
                return json.dumps(response)


    ### HELPERS ###

    def __valid_put_data(self, ui_load: dict, method) -> bool:
        """Validates that ui_load contains data for 1 employee and that an id is provided, Also used for delete"""
        
        # Check if id is key in main dict
        try:
            id_ = ui_load['id']

            # Check if id is empty
            if not id_:
                raise NoIdException(self._key, method)

            # ui_load is valid for put request
            else:
                return True

        # Raise custom Exception
        except KeyError:
            raise IncorrectInputException(self._key, method)

    def __is_new(self, data: json) -> bool:
        """
        Used in POST exception handling
        """
        ui_load = json.loads(data)['data']
        unique_val = ui_load[self._unique]

        # Parse DB response
    
        data_load = json.loads(self.get_all(data))

        if not data_load["type"]:
            return True
        
        data_load = data_load["data"]
        # Search submitted unique_val address in DB
        for val in data_load.values():
            if val[self._unique] == unique_val:
                return False

        return True

    def __is_boss(self, data: json) -> bool:
        """Used in POST, PUT, DELETE exception handling"""
        return json.loads(data)['role'] == 'boss'

    def __wants_filter(self, data: json) -> bool:
        """If 'filter' field is set we return the field to filter and value"""
        return 'filter' in json.loads(data)['data'].keys()

    def __correct_fields(self, data: json) -> bool:
        """
        Used in POST
        
        Checks if required fields are submitted and not empty
        """
        ui_load = json.loads(data)['data']
        if self._required.issubset(ui_load.keys()):
            for key in self._required:
                if not ui_load[key]:
                    return False
            return True
        return False

    def __autofill_input(self, data: json) -> json:
        
        # Parse user input
        ui_load = json.loads(data)

        # Iterate through fields with registered autofill values
        for key, val in self._autofill.items():

            # __correct_fields() returns False if data contains empty values
            # so here it suffices to autofill key-val pairs where key doesn't exist in ui_load
            if not key in ui_load['data'].keys():
                ui_load['data'][key] = val

        return json.dumps(ui_load)
                
