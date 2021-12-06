import json
from Data.DataAPI import DataAPI
from Exceptions import *

class Base:

    def __init__(self, key, identifier) -> None:
        self.__data_api = DataAPI()
        self.__key = key
        self.__identifier = identifier


    ### CRUD ###

    def get_all(self, data: json) -> json:
        return self.__data_api.get_all(data)

    def get(self, data: json) -> json:
        pass

    def post(self, data: json) -> json:
        if self.__is_boss(data):
            
            if self.__is_new(data):
                return self.__data_api.post(data)
            
            else:
                raise DataAlreadyExistsException(self.__key, 'POST')
        else:
            raise UnauthorizedRequestException(self.__key, 'POST')

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
                fixed_data = json.dumps({"key": self.__key, "data": data_load})
                response = json.loads(self.__data_api.put(fixed_data))

                # Return fixed data to UI to be displayed
                if response['type']:
                    response['data'] = data_load[id_]

                    return json.dumps(response)

        else:
            raise UnauthorizedRequestException(self.__key, 'PUT')

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
                    raise IncorrectIdException(self.__key, 'DELETE')
                #make put request with all data exept given load
                fixed_data = json.dumps({"key": self.__key, "data": data_load})
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
                raise NoIdException(self.__key, method)

            # ui_load is valid for put request
            else:
                return True

        # Raise custom Exception
        except KeyError:
            raise IncorrectInputException(self.__key, method)

    def __is_new(self, data: json) -> bool:
        """
        Used in POST exception handling
        """
        ui_load = json.loads(data)['data']
        identifier = ui_load[self.__identifier]

        # Parse DB response
    
        data_load = json.loads(self.get_all(data))

        if not data_load["type"]:
            return True
        
        data_load = data_load["data"]
        # Search submitted identifier address in DB
        for val in data_load.values():
            if val[self.__identifier] == identifier:
                return False

        return True

    def __is_boss(self, data: json) -> bool:
        """Used in POST, PUT, DELETE exception handling"""
        return json.loads(data)['role'] == 'boss'






