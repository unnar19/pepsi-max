from Logic.LogicAPI import LogicAPI
import json

class InteractionsUI:
    def __init__(self):
        self.LL = LogicAPI()

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
        request = json.dumps({'key': 'employee','data':{'id': id_str}})
        response = self.LL.get(request)

        response_dict = json.loads(response)
        data_dict = response_dict['data']

        first_name = data_dict['name'].split(' ')
        first_name = first_name[0]

        name = [f'{"Name:":<15}{data_dict["name"]}','','','']
        email = [f'{"Email:":<15}{data_dict["email"]}','','','']
        id = [f'{"ID:":<15}{data_dict["id"]}','','','']
        ssn = [f'{"SSN:":<15}{data_dict["ssn"]}','','','']
        h_phone = [f'{"Phone:":<15}{data_dict["home_phone"]}','','','']
        m_phone = [f'{"":<15}{data_dict["mobile_phone"]}','','','']
        location = [f'{"Location:":<15}{data_dict["destination"]}','','','']
        
        ret = [name,email,id,ssn,h_phone,m_phone,location]
        for _ in range(len(ret),20):
            ret.append([''])
        return first_name, ret