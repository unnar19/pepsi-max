from UI.ScreensUI import ScreensUI
from Logic.LogicAPI import LogicAPI
import json

class EmployeeUI:
    def __init__(self) -> None:
        self.screen = ScreensUI()
        self.logic_api = LogicAPI()

    def authenticate_login(self, email, password):
        data_dict = {
            'key': 'employee',
            'data': {
                'email': email,
                'password': password
            }
        }
        data = json.dumps(data_dict)
        response = self.logic_api.authenticate_employee(data)

        if not response:
            return False, 1, 1, 1
        response_dict = json.loads(response)
        id = response_dict['data']['id']
        role = response_dict['data']['role']
        name = response_dict['data']['name']
        return True, id, role, name

    def login_screen(self, first_login):
        self.screen.format.subtitle = 'Log-in Screen'
        self.screen.format.edit_commands(['Email','Password','Log-in'])
        list_of_comments = ['Enter email address', 'Enter password'] 
        self.screen.format.apply_styles([0,0,1])
        if not first_login:
            self.screen.format.comment = 'User doesnt exist, Select an option'
        while True:
            self.screen.format.print_screen()
            input_str = self.screen.get_input('Input')
            input_int, type_of_input = self.screen.check_type_of_input(input_str)
            if type_of_input == 0:
                self.screen.format.comment = list_of_comments[input_int]
                self.screen.format.print_screen()
                input_str = self.screen.get_input('Text input')
                self.screen.format.change_text_box(input_int, input_str)
            elif type_of_input == 1:
                email = self.screen.format.commands['Email'][1][1:-1]
                print(email)
                password = self.screen.format.commands['Password'][1][1:-1]
                print(password)
                return self.authenticate_login(email, password)

            if not str(type_of_input).isdigit():
                self.screen.format.comment = f'{type_of_input}, Select an option'
            else:
                self.screen.format.comment = 'Select an option'


