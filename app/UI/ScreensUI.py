from os import name
from UI.FormatUI import FormatUI
import json
from UI.InteractionsUI import InteractionsUI

class ScreensUI():
    def __init__(self):
        self.format = FormatUI()
        self.inter = InteractionsUI()
        self.id = 'boss'

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

                logged_in, self.id, self.role, self.name = self.inter.authenticate_login(email, password)
                if not logged_in:
                    return False
                first_name = self.name.split(' ')
                first_name = first_name[0]
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

    def employees_screen(self) -> None:      
        self.format.preview_title = f'{"Name":<30} | {"ID":<5} | {"Phone":<10} | {"Location":<12}'
        search_str = self.format.styles[0][1:-1]
        self.format.comment = 'Select an option'
        list_of_comments = ['Enter search term']
        curr_page = 1
        self.emp_list = self.inter.listing_all_employees()
        id_list = []
        [id_list.append(employee[1])for employee in self.emp_list]
        # Make list for each screen
        self.page_list = self.screen_lists_from_all(self.emp_list)

        while True:
            if self.filter_str == '':
                self.format.preview_comment = f'Page {curr_page} of {len(self.page_list)} | Filter: [empty]'
            self.format.subtitle = 'Menu > Employees'
            self.format.edit_commands(['Search','Filter','Select','Prev page','Next page','Back'])
            self.format.apply_styles([0,1,1,1,1,1])
            self.format.update_text_box(0, search_str)

            self.format.listing_lis = self.page_list[curr_page-1]

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
                    curr_page = 1
                    self.filter_screen()
                    self.format.preview_comment = f'Page {curr_page} of {len(self.page_list)} | Filter: [{self.filter_str}]'
                    self.format.comment = 'Select an option'

                elif input_int == 2: # Select employee
                    self.format.comment = 'Enter ID of employee'
                    self.format.print_screen()
                    id_input = self.get_input('Input')
                    if id_input in id_list:
                        self.profile_screen(id_input)
                        self.emp_list = self.inter.listing_all_employees()
                        id_list = []
                        [id_list.append(employee[1])for employee in self.emp_list]
                        # Make list for each screen again
                        self.page_list = self.screen_lists_from_all(self.emp_list)
                        self.filter_str = ''
                        curr_page = 1

                    else:
                        self.format.comment = 'ID not valid, Select an option'
                    self.format.preview_title = f'{"Name":<30} | {"ID":<5} | {"Phone":<10} | {"Location":<12}'
                    self.format.preview_comment = f'Page {curr_page} of {len(self.page_list)} | Filter: [{self.filter_str}]'
                    
                elif input_int == 3: # Previous Page
                    if curr_page > 1:
                        self.format.comment = 'Select an option'
                        curr_page -= 1
                    else:
                        self.format.comment = 'Invalid input, Select an option'
                
                elif input_int == 4: # Next Page
                    if curr_page < len(self.page_list):
                        self.format.comment = 'Select an option'
                        curr_page += 1
                    else:
                        self.format.comment = 'Invalid input, Select an option'

                elif input_int == 5: #Back (goes to back the the main menu)
                    self.format.listing_lis = self.format.empty_listing()
                    self.format.comment = 'Select an option'
                    return

    def profile_screen(self, id_str):
        self.format.comment = 'Select an option'
        self.format.profile = True
        while True:
            self.format.subtitle = 'Menu > Employees > Select'
            self.format.edit_commands(['Edit info','Tickets','Back'])
            self.format.apply_styles([1,1,1])
            self.format.preview_title = 'Employee information'
            name, self.format.listing_lis = self.inter.custom_individual_preview(id_str)
            self.format.preview_comment = f"There are 10 days until {name}'s birthday"
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            else:
                if input_int == 0: # Edit info
                    self.edit_profile(id_str)
                elif input_int == 1: # Tickets?
                    self.format.comment = 'Select an option' # ALSO JUST GOES BACK
                    self.format.profile = False
                    return
                elif input_int == 2: # Back
                    self.format.comment = 'Select an option'
                    self.format.profile = False
                    return

    def edit_profile(self, id_str):
        self.format.subtitle = 'Menu > Employees > Select > Edit info'
        self.format.edit_commands(['Name','Email','Home phone','Mobile phone','Location','Apply Changes','Cancel'])
        self.format.apply_styles([0,0,0,0,0,1,1])
        user_data_dict = self.inter.get_individual(id_str)
        
        # Set new values to the original ones
        new_name = user_data_dict['name']
        new_email = user_data_dict['email']
        new_h_phone = user_data_dict['home_phone']
        new_m_phone = user_data_dict['mobile_phone']
        new_location = user_data_dict['destination']       

        while True:
            self.format.update_text_box(0,new_name)
            self.format.update_text_box(1,new_email)
            self.format.update_text_box(2,new_h_phone)
            self.format.update_text_box(3,new_m_phone)
            self.format.update_text_box(4,new_location)

            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            elif type_of_input == 1:
                if input_int == 5: # Apply changes
                    new_data_dict = {'id': user_data_dict['id'],'name':new_name, 'email': new_email, 'home_phone': new_h_phone, 'mobile_phone': new_m_phone, 'destination': new_location}
                    edit_response = self.inter.edit_employee(self.id, new_data_dict)
                    if not edit_response:
                        self.format.comment = 'Unauthorized, Select an option'
                    else:
                        name, self.format.listing_lis = self.inter.custom_individual_preview(new_data_dict['id'])
                        return
                elif input_int == 6: # Cancel
                    self.format.comment = 'Select an option'
                    return
            elif type_of_input == 0:
                if input_int == 0: # Name
                    self.format.comment = 'Enter new name'
                    self.format.print_screen()
                    new_name = self.get_input('Text input')
                    self.format.comment = 'Select an option'
                elif input_int == 1: # Email
                    self.format.comment = 'Enter new email address'
                    self.format.print_screen()
                    new_email = self.get_input('Text input')
                    self.format.comment = 'Select an option'
                elif input_int == 2: # Home phone
                    self.format.comment = 'Enter new home phone number'
                    self.format.print_screen()
                    new_h_phone = self.get_input('Text input')
                    self.format.comment = 'Select an option'
                elif input_int == 3: # Mobile phone
                    self.format.comment = 'Enter new mobile phone number'
                    self.format.print_screen()
                    new_m_phone = self.get_input('Text input')
                    self.format.comment = 'Select an option'
                elif input_int == 4: # Location
                    self.format.comment = 'Enter new location'
                    self.format.print_screen()
                    new_location = self.get_input('Text input')
                    self.format.comment = 'Select an option'
    

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
            self.page_list = self.screen_lists_from_all(self.emp_list)
            self.filter_str = ''
        elif input_int == 7: # Back
            self.format.comment = 'Select an option'
        else: # Filter selected
            list_of_commands = list(self.format.commands)
            self.filter_str = list_of_commands[input_int]
            listing_list = self.inter.filter_listing(self.filter_str,'destination')
            self.page_list = self.screen_lists_from_all(listing_list)
            