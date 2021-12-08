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

    def listing_all_real_estates(self) -> list:
        ''' Gets all realestates and their information to display when listing'''

        # Request data drom API
        request = json.dumps({'key': 'real_estate'})
        response = self.LL.get_all(request)
        response_dict = json.loads(response)

        # Decode dictionary to nested lists
        real_estate_list = []
        for value in response_dict['data'].values():
            nested_real_list = []
            nested_real_list.append(value['address'])
            nested_real_list.append(value['id'])
            nested_real_list.append(value['real_estate_id'])
            nested_real_list.append(value['destination'])
            real_estate_list.append(nested_real_list)
        return real_estate_list

    def filter_listing(self, filter_str, key, filter_type):
        request = json.dumps({'key': key, "filter": True, 'data':{'filter': filter_type, 'filter_value': filter_str}})
        response = self.LL.get_all(request)
        response_dict = json.loads(response)

        if key == 'employee':
            value_list = ['name','id','mobile_phone','destination']
        elif key == 'real_estate':
            value_list = ['address','id','real_estate_id','destination']

        big_list = []
        for value in response_dict['data'].values():
            nested_line_list = []
            for item in value_list:
                nested_line_list.append(value[item])
            big_list.append(nested_line_list)
        return big_list

    def get_person(self, id_str):
        '''
        Takes in a legal id of an employee and recieves all information
        '''
        request = json.dumps({'key': 'employee','data':{'id': id_str}})
        response = self.LL.get(request)

        response_dict = json.loads(response)
        data_dict = response_dict['data']
        return data_dict

    def custom_person_preview(self, id_str):
        '''
        Takes in a legal id of an employee and recieves all information
        from employee line stored. Then formats lists to put into custom
        preview screen ( Profile information screen )
        '''
        data_dict = self.get_person(id_str)
        first_name = data_dict['name'].split(' ')[0]

        # Puts recieved data into individual lists for ScreensUI
        name = [f'{"Name:":<15}{data_dict["name"]}']
        email = [f'{"Email:":<15}{data_dict["email"]}']
        ssn = [f'{"SSN:":<15}{data_dict["ssn"]}']
        id = [f'{"ID:":<15}{data_dict["id"]}']
        
        h_phone = [f'{"Home phone:":<15}{data_dict["home_phone"]}']
        m_phone = [f'{"Mobile phone:":<15}{data_dict["mobile_phone"]}']
        location = [f'{"Location:":<15}{data_dict["destination"]}']
        address = [f'{"Address:":<15}{data_dict["address"]}']
        
        custom_preview = [name,email,ssn,id,[''],h_phone,m_phone,location,address]
        for _ in range(len(custom_preview),20):
            custom_preview.append([''])
        return first_name, custom_preview

    def edit_profile(self, role_of_user, key, new_data_dict):
        request = json.dumps({'key': key, 'role': role_of_user, 'data': new_data_dict})
        response = self.LL.put(request)
        response_dict = json.loads(response)
        return response_dict['type']

    def add_profile(self, role_of_user, key, new_data_dict):
        request = json.dumps({'key': key, 'role': role_of_user, 'data': new_data_dict})
        print(request)
        input('stop')
        response = self.LL.post(request)
        response_dict = json.loads(response)
        print(response_dict)
        input('stop')
        return response_dict['type']

    def get_real_estate(self, id_str):
        '''
        Takes in a legal id of a real estate and recieves all information
        '''
        request = json.dumps({'key': 'real_estate','data':{'id': id_str}})
        response = self.LL.get(request)

        response_dict = json.loads(response)
        data_dict = response_dict['data']
        return data_dict

    def custom_real_estate_preview(self, id_str):
        data_dict = self.get_real_estate(id_str)

        # Puts recieved data into individual lists for ScreensUI
        address = [f'{"Address:":<15}{data_dict["address"]}']
        location = [f'{"Location:":<15}{data_dict["destination"]}']
        address_id = [f'{"Address ID:":<15}{data_dict["real_estate_id"]}']
        id = [f'{"ID:":<15}{data_dict["id"]}']
        
        maintenance = [f'{"Maintenance:":<15}{data_dict["maintenance_info"]}']
        
        custom_preview = [address,location,address_id,id,[''],maintenance]
        for _ in range(len(custom_preview),20):
            custom_preview.append([''])
        return custom_preview