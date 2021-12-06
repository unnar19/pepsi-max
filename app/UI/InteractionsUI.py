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

    def check_id(self, id_input):
        request = json.dumps({'key': 'employee', 'data':{'id': id_input}})
        response = self.LL.authenticate_employee(request)
        print(response)



