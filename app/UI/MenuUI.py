from UI.FormatUI import FormatUI
from UI.InteractionsUI import InteractionsUI
from UI.EmployeeUI import EmployeeUI
from UI.RealEstateUI import RealEstateUI
from UI.TicketUI import TicketUI
from UI.ReportUI import ReportUI
from UI.ContractorsUI import ContractorsUI
from UI.DestinationUI import DestinationUI


class MenuUI():
    def __init__(self):
        self.format = FormatUI()
        self.inter = InteractionsUI()
        self.id = 1
        self.role = 'boss'
        self.destination = 'Reykjavík'
    
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

    def screen_lists_from_all(self, listing_list) -> list:
        ''' Splits listing list into pages '''
        maximum = 20
        page_count = (len(listing_list) // maximum) + 1 
        if len(listing_list) % maximum == 0:
            page_count -= 1

        page_list = []
        offset = 0
        for page_i in range(page_count):
            if page_i == page_count-1:
                last_page = listing_list[(page_i)*offset:]
                remaining = maximum - len(last_page)
                if remaining == 0:
                    remaining = 19
                [last_page.append(['','','','']) for _ in range(remaining)]

                page_list.append(last_page)
            else:
                page_list.append(listing_list[(page_i-1)*offset:maximum + offset])
                offset += 20
        return page_list

    def str2bool(self, boolean_string : str) -> bool:
        return boolean_string.lower() in ["yes", "true", "t", "1"]

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

                logged_in, self.id, self.role, self.name, self.destination = self.inter.authenticate_login(email, password)
                if not logged_in:
                    return False

                first_name = self.name.split(' ')[0]
                logged_str = f'Logged in as: {first_name}'
                self.format.title += f'{logged_str:>42}'
                return True

            if not str(type_of_input).isdigit():
                self.format.comment = f'{type_of_input}, Select an option'
            else:
                self.format.comment = 'Select an option'

    def menu_screen(self):
        self.format.comment = 'Select an option'
        while True:
            self.format.subtitle = 'Menu'
            self.format.edit_commands(['Employees','Real Estate','Tickets','Reports','Contractors','Destinations','Log-out'])
            self.format.apply_styles([1,1,1,1,1,1,1])
            self.format.preview_title = ''
            self.format.preview_comment = ''
            self.format.print_screen()
        
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            elif input_int == 0: #employees
                EmployeeUI(self.id,self.role,self.destination).employees_screen()
            elif input_int == 1: #realestate
                RealEstateUI(self.id,self.role,self.destination).real_estate_screen()
            elif input_int == 2: # Tickets
                TicketUI(self.id,self.role,self.destination).tickets_screen()
            elif input_int == 3: # Reports
                ReportUI(self.id,self.role,self.destination).reports_screen()
            elif input_int == 4: #contractors
                ContractorsUI(self.id,self.role,self.destination).contractors_screen()
            elif input_int == 5: # Destinations
                DestinationUI(self.id,self.role,self.destination)#.destinations_screen()
            elif input_int == 6: #log out
                return False