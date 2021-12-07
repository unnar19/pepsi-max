from Logic.LogicAPI import LogicAPI
import json

class InteractionsUI:
    def __init__(self):
        '''
        InteractionsUI contains all methods that communicate to
        the logic layer wrapper ( LogicAPI() ) to make ScreensUI
        more readable.

        All methods use json encoding and decoding
        '''
        self.LL = LogicAPI()
    
    def authenticate_login(self, email, password):
        '''
        
        '''
        data_dict = {
            'key': 'employee',
            'data': {
                'email': email,
                'password': password
            }
        }
        data = json.dumps(data_dict)
        response = self.LL.authenticate_employee(data)
        response_dict = json.loads(response)

        if not response_dict['type']:
            return False, None, None, None
        
        id = response_dict['data']['id']
        role = response_dict['data']['role']
        name = response_dict['data']['name']
        return True, id, role, name

    def listing_all_employees(self) -> list:
        ''' Gets all employees and their information to display when listing'''

        # Request data drom API
        request = json.dumps({'key': 'employee'})
        response = self.LL.get_all(request)
        response_dict = json.loads(response)

        # Decode dictionary to nested lists
        employee_list = []
        for value in response_dict['data'].values():
            nested_emp_list = []
            nested_emp_list.append(value['name'])
            nested_emp_list.append(value['id'])
            nested_emp_list.append(value['mobile_phone'])
            nested_emp_list.append(value['destination'])
            employee_list.append(nested_emp_list)
        return employee_list

    def filter_listing(self, filter_str, filter_type):
        request = json.dumps({'key': 'employee', "filter": True, 'data':{'filter': filter_type, 'filter_value': filter_str}})
        response = self.LL.get_all(request)
        response_dict = json.loads(response)

        employee_list = []
        for value in response_dict['data'].values():
            nested_emp_list = []
            nested_emp_list.append(value['name'])
            nested_emp_list.append(value['id'])
            nested_emp_list.append(value['mobile_phone'])
            nested_emp_list.append(value['destination'])
            employee_list.append(nested_emp_list)
        return employee_list

    def get_individual(self, id_str):
        '''
        Takes in a legal id of an employee and recieves all information
        from employee line stored.
        '''
        request = json.dumps({'key': 'employee','data':{'id': id_str}})
        response = self.LL.get(request)

        response_dict = json.loads(response)
        data_dict = response_dict['data']
        return data_dict

    def custom_individual_preview(self, id_str):
        '''
        Takes in a legal id of an employee and recieves all information
        from employee line stored. Then formats lists to put into custom
        preview screen ( Profile information screen )
        '''
        data_dict = self.get_individual(id_str)
        first_name = data_dict['name'].split(' ')[0]

        # Puts recieved data into individual lists for ScreensUI
        name = [f'{"Name:":<15}{data_dict["name"]}']
        email = [f'{"Email:":<15}{data_dict["email"]}']
        id = [f'{"ID:":<15}{data_dict["id"]}']
        ssn = [f'{"SSN:":<15}{data_dict["ssn"]}']
        h_phone = [f'{"Phone:":<15}{data_dict["home_phone"]}']
        m_phone = [f'{"":<15}{data_dict["mobile_phone"]}']
        location = [f'{"Location:":<15}{data_dict["destination"]}']
        
        custom_preview = [name,email,id,ssn,h_phone,m_phone,location]
        for _ in range(len(custom_preview),20):
            custom_preview.append([''])
        return first_name, custom_preview

    def edit_employee(self, role_of_user, new_data_dict):
        request = json.dumps({'key': 'employee', 'role': role_of_user, 'data': new_data_dict})
        response = self.LL.put(request)
        response_dict = json.loads(response)
        return response_dict['type']
        