from UI.FormatUI import FormatUI
from Logic.LogicAPI import LogicAPI
import json

class ScreensUI():
    def __init__(self):
        self.format = FormatUI()
        self.logic_api = LogicAPI()

    def get_input(self, prompt_str):
        return input(f' {prompt_str}: ')

    def check_type_of_input(self, input_str):
        if input_str.isdigit():
            input_int = int(input_str)-1
            if input_int < len(self.format.commands) and input_int >= 0:
                list_of_options = list(self.format.commands)
                if self.format.commands[list_of_options[input_int]][1] == self.format.styles[1]: # Command
                    return input_int, 1
                elif self.format.commands[list_of_options[input_int]][1] == self.format.styles[2]: # CheckBox
                    return input_int, 2
                elif self.format.commands[list_of_options[input_int]][1] == self.format.styles[3]: # Filled CheckBox
                    return input_int, 3
                else: # Textbox
                    return input_int, 0
            else:
                return None, 'Input out of range' #number not in range of options
        else: 
            return None, 'Invalid input' #not a menu selection

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
    
    def login_screen(self, first_login) -> bool: 
        self.format.subtitle = 'Log-in Screen'
        self.format.reset_title()
        self.format.preview_title = ''
        self.format.preview_comment = ''
        self.format.edit_commands(['Email','Password','Log-in'])
        list_of_comments = ['Enter email address', 'Enter password'] 
        self.format.apply_styles([0,0,1])
        if not first_login:
            self.format.comment = 'User doesnt exist, Select an option'
        while True:
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type_of_input == 0:
                self.format.comment = list_of_comments[input_int]
                self.format.print_screen()
                input_str = self.get_input('Text input')
                self.format.update_text_box(input_int, input_str)
            elif type_of_input == 1:
                email = self.format.commands['Email'][1][1:-1]
                print(email)
                password = self.format.commands['Password'][1][1:-1]
                print(password)

                logged_in, self.id, self.role, self.name = self.authenticate_login(email, password)
                logged_str = f'Logged in as: {self.name}'
                self.format.title += f'{logged_str:>42}'
                return logged_in

            if not str(type_of_input).isdigit():
                self.format.comment = f'{type_of_input}, Select an option'
            else:
                self.format.comment = 'Select an option'

    def menu_screen(self):
        self.format.comment = 'Select an option'
        while True:
            self.format.subtitle = 'Menu'
            self.format.edit_commands(['Employees','Real Estate','Maintenance','Contractors','Log-out'])
            self.format.apply_styles([1,1,1,1,1])
            self.format.preview_title = ''
            self.format.preview_comment = ''
            self.format.print_screen()
        
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            elif input_int == 0: #employees
                self.filter_str = ''
                self.employees_screen()
            elif input_int == 1: #realestate
                print('Realestate screen')
                input('continue?')
            elif input_int == 2: #maintenance
                print('maintenance screen')
                input('continue?')
            elif input_int == 3: #contractors
                print('contractors screen')
                input('continue?')
            elif input_int == 4: #log out
                return False

    def employees_screen(self) -> None:      
        self.format.preview_title = f'{"Name":<23} | {"ID":<5} | {"Phone":<15} | {"Location":<12}'
        search_str = self.format.styles[0][1:-1]
        self.format.comment = 'Select an option'
        list_of_comments = ['Enter search term']
        while True:
            if self.filter_str == '':
                self.format.preview_comment = 'Page 1 of 1 | Filter: [empty]'
            self.format.subtitle = 'Menu > Employees'
            self.format.edit_commands(['Search','Filter','Select','Next page','Prev page','Back'])
            self.format.apply_styles([0,1,1,1,1,1])
            self.format.update_text_box(0, search_str)
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)

            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'

            elif type_of_input == 0: #Search (form of accurate filtering)
                self.format.comment = list_of_comments[input_int]
                self.format.print_screen()
                search_str = self.get_input('Text input')
                self.format.update_text_box(input_int, search_str)
                self.format.comment = 'Select an option'

            elif type_of_input == 1:
                if input_int == 1: # Filters
                    self.format.comment = 'Select a filter'
                    self.filter_screen()
                    self.format.comment = 'Select an option'

                elif input_int == 1: # Select employee
                    pass
                elif input_int == 1: # Next Page
                    pass
                elif input_int == 1: # Previous Page
                    pass
                elif input_int == 5: #Back (goes to back the the main menu)
                    self.format.comment = 'Select an option'
                    return

    def filter_screen(self):
        self.format.subtitle = 'Menu > Employees > Filter'
        self.format.edit_commands(['Kulusuk','Longyearbyen','Nuuk','Reykjavík','Tingwall','Tórshavn','Clear','Back'])
        self.format.apply_styles([1,1,1,1,1,1,1,1])
        self.format.print_screen()
        input_str = self.get_input('Input')
        input_int, type_of_input = self.check_type_of_input(input_str)
        if type(type_of_input) != int:
            self.format.comment = f'{type_of_input}, Select a filter'
            self.filter_screen()
        elif input_int == 6: # Clear
            self.format.comment = 'Select an option'
            self.filter_str = ''
        elif input_int == 7: # Back
            self.format.comment = 'Select an option'
        else: # Filter selected
            list_of_commands = list(self.format.commands)
            self.filter_str = list_of_commands[input_int]
            self.format.preview_comment = f'Page 1 of 1 | Filter: [{self.filter_str}]'