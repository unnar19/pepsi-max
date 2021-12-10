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
        destination = response_dict['data']['destination']
        return True, id, role, name, destination

    def listing_all_employees(self) -> list:
        ''' Gets all employees and their information to display when listing'''

        # Request data drom API
        request = json.dumps({'key': 'employee','data':{}})
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
        request = json.dumps({'key': 'real_estate','data':{}})
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


    def listing_all_contractors(self) -> list:
        ''' Gets all contractors and their information to display when listing'''

        # Request data drom API
        request = json.dumps({'key': 'contractor','data':{}})
        response = self.LL.get_all(request)
        response_dict = json.loads(response)

        # Decode dictionary to nested lists
        contractor_list = []
        for value in response_dict['data'].values():
            nested_cont_list = []
            nested_cont_list.append(value['name'])
            nested_cont_list.append(value['id'])
            nested_cont_list.append(value['phone'])
            nested_cont_list.append(value['destination'])
            contractor_list.append(nested_cont_list)
        return contractor_list


    def listing_all_for_destination(self, key, destination) -> list:
        ''' Gets all X and their information to display when listing'''

        # Request data drom API
        request = json.dumps({'key': key, 'filter': True, 'data':{'filter':'destination', 'filter_value': destination}})
        response = self.LL.get_all(request)
        response_dict = json.loads(response)

        if key == 'ticket':
            value_list = ['description','id','real_estate_id','closed']
        elif key == 'report':
            value_list = ['description','id','real_estate_id','approved']

        # Decode dictionary to nested lists
        real_estate_list = []
        for value in response_dict['data'].values():
            nested_real_list = []
            for v in value_list:
                nested_real_list.append(value[v])
            real_estate_list.append(nested_real_list)
        return real_estate_list

    def listing_all_destinations(self) -> list:
        ''' Gets all destinations and their information to display when listing'''

        # Request data drom API
        request = json.dumps({'key': 'destination','data':{}})
        response = self.LL.get_all(request)
        response_dict = json.loads(response)

        # Decode dictionary to nested lists
        destination_list = []
        for value in response_dict['data'].values():
            nested_destination_list = []
            nested_destination_list.append(value['airport'])
            nested_destination_list.append(value['id'])
            nested_destination_list.append(value['country'])
            nested_destination_list.append(value['manager_id'])
            destination_list.append(nested_destination_list)
        return destination_list

    def filter_listing(self, filter_str, key, filter_type):
        request = json.dumps({'key': key, "filter": True, 'data':{'filter': filter_type, 'filter_value': filter_str}})
        response = self.LL.get_all(request)
        response_dict = json.loads(response)

        if key == 'employee':
            value_list = ['name','id','mobile_phone','destination']
        elif key == 'real_estate':
            value_list = ['address','id','real_estate_id','destination']
        elif key == 'contractor':
            value_list = ['name','id','phone','destination']

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

    def get_ticket_or_report(self,key, id_str):
        '''
        Takes in a legal id of a ticket or report and recieves all information
        '''
        request = json.dumps({'key': key,'data':{'id': id_str}})
        response = self.LL.get(request)

        response_dict = json.loads(response)
        data_dict = response_dict['data']
        return data_dict

    def custom_ticket_preview(self, id_str):
        data_dict = self.get_ticket_or_report('ticket',id_str)

        # Puts recieved data into individual lists for ScreensUI
        description = [f'{"Description:":<15}{data_dict["description"]}']
        start = [f'{"Start date:":<15}{data_dict["start_date"]}']
        close = [f'{"Close date:":<15}{data_dict["close_date"]}']
        id = [f'{"ID:":<15}{data_dict["id"]}']

        estate_id = [f'{"Address ID:":<15}{data_dict["real_estate_id"]}']
        employee_id = [f'{"Employee ID:":<15}{data_dict["employee_id"]}']
        report_id = [f'{"Report ID:":<15}{data_dict["report_id"]}']
        contractor_id = [f'{"Contractor ID:":<15}{data_dict["contractor_id"]}']

        location = [f'{"Location:":<15}{data_dict["destination"]}']
        
        priority = [f'{"Priority:":<15}{data_dict["priority"]}']
        ready = [f'{"Ready:":<15}{data_dict["ready"]}']
        closed = [f'{"Closed:":<15}{data_dict["closed"]}']
        recurring = [f'{"Recurring:":<15}{data_dict["is_recurring"]}']


        custom_preview = [description,start,close,id,[''],estate_id,employee_id,report_id,contractor_id,[''],location,[''],priority,ready,closed,recurring]
        for _ in range(len(custom_preview),20):
            custom_preview.append([''])
        return custom_preview

    def custom_report_preview(self, id_str):
        data_dict = self.get_ticket_or_report('report',id_str)
        print(data_dict)
        input('stop')
        # Puts recieved data into individual lists for ScreensUI
        description = [f'{"Description:":<15}{data_dict["description"]}']
        date = [f'{"Date:":<15}{data_dict["date"]}']
        ticket_id = [f'{"Ticket ID:":<15}{data_dict["ticket_id"]}']
        id = [f'{"ID:":<15}{data_dict["id"]}']
        
        real_estate_id = [f'{"Address ID:":<15}{data_dict["real_estate_id"]}']  
        employee_id = [f'{"Employee ID:":<15}{data_dict["employee_id"]}']
        destination = [f'{"Location:":<15}{data_dict["destination"]}']

        contractor_id = [f'{"Contractor ID:":<15}{data_dict["contractor_id"]}']
        contractor_pay = [f'{"Contractor pay:":<15}{data_dict["contractor_pay"]}']
        price = [f'{"Total cost:":<15}{data_dict["total_price"]}']
        
        approved = [f'{"Approved:":<15}{data_dict["approved"]}']
        comments = [f'{"Comment:":<15}{data_dict["comments"]}']

        custom_preview = [description,date,ticket_id,id,[''],real_estate_id,employee_id,destination,[''],contractor_id,contractor_pay,price,[''],approved,comments]
        for _ in range(len(custom_preview),20):
            custom_preview.append([''])
        return custom_preview


    def edit_profile(self, role_of_user, key, new_data_dict):
        request = json.dumps({'key': key, 'role': role_of_user, 'data': new_data_dict})
        response = self.LL.put(request)
        response_dict = json.loads(response)
        return response_dict['type']

    def add_profile(self, role_of_user, key, new_data_dict):
        '''
        Works for any key
        '''
        request = json.dumps({'key': key, 'role': role_of_user, 'data': new_data_dict})
        response = self.LL.post(request)
        response_dict = json.loads(response)
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

    def get_destination(self, id_str):
        '''
        Takes in a legal id of a destination and recieves all information
        '''
        request = json.dumps({'key': 'destination','data':{'id': id_str}})
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

    def custom_destination_preview(self, id_str):
        data_dict = self.get_destination(id_str)

        # Puts recieved data into individual lists for ScreensUI
        name = [f'{"Name:":<15}{data_dict["name"]}']
        airport = [f'{"Airport:":<15}{data_dict["airport"]}']
        country = [f'{"Country:":<15}{data_dict["country"]}']
        phone = [f'{"Phone:":<15}{data_dict["phone"]}']
        opening_hours = [f'{"Opening hours:":<15}{data_dict["opening_hours"]}']
        manager_id = [f'{"Manager ID:":<15}{data_dict["manager_id"]}']
        id = [f'{"ID:":<15}{data_dict["id"]}']
        
        custom_preview = [name,airport,country,phone,opening_hours,manager_id,id]
        for _ in range(len(custom_preview),20):
            custom_preview.append([''])
        return custom_preview

    def get_contractor(self, id_str):
        '''
        Takes in a legal id of a contractor and recieves all information
        '''
        request = json.dumps({'key': 'contractor','data':{'id': id_str}})
        response = self.LL.get(request)

        response_dict = json.loads(response)
        data_dict = response_dict['data']
        return data_dict

    def custom_contractor_preview(self, id_str):
        '''
        Takes in a legal id of a contractor and recieves all information
        from contractor line stored. Then formats lists to put into custom
        preview screen ( Profile information screen )
        '''
        data_dict = self.get_contractor(id_str)

        # Puts recieved data into individual lists for ScreensUI
        name = [f'{"Name:":<15}{data_dict["name"]}']
        contact = [f'{"Contact info:":<15}{data_dict["contact"]}']
        phone = [f'{"Phone:":<15}{data_dict["phone"]}']
        id = [f'{"ID:":<15}{data_dict["id"]}']
        opening_hours = [f'{"Opening hours:":<15}{data_dict["opening_hours"]}']
        location = [f'{"Location:":<15}{data_dict["destination"]}']

        tickets = [f'{"Tickets:":<15}{data_dict["tickets"]}']
        
        custom_preview = [name,contact,phone,id,opening_hours,location,[''],tickets]
        for _ in range(len(custom_preview),20):
            custom_preview.append([''])
        return custom_preview