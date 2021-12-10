from UI.FormatUI import FormatUI
from UI.InteractionsUI import InteractionsUI

class RealEstateUI:
    def __init__(self,id,role,location) -> None:
        self.format = FormatUI()
        self.inter = InteractionsUI()
        self.id = id
        self.role = role
        self.destination = location
        self.filter_str = ''

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

    def real_estate_screen(self):
        self.format.preview_title = f'{"Address":<30} | {"ID":<5} | {"Address ID":<10} | {"Location":<12}'
        search_str = self.format.styles[0][1:-1]
        self.format.comment = 'Select an option'
        list_of_comments = ['Enter search term']
        curr_page = 1
        self.emp_list = self.inter.listing_all_real_estates()
        id_list = []
        [id_list.append(estate[1])for estate in self.emp_list]
        # Make list for each screen
        self.page_list = self.screen_lists_from_all(self.emp_list)

        while True:
            if self.filter_str == '':
                self.format.preview_comment = f'Page {curr_page} of {len(self.page_list)} | Filter: [empty]'
            self.format.subtitle = 'Menu > Real Estate'
            self.format.edit_commands(['Search','Filter','Select','Prev page','Next page','Add Real Estate','Back'])
            self.format.apply_styles([0,1,1,1,1,1,1])
            self.format.update_text_box(0, search_str)

            if len(self.page_list) == 0:
                self.format.listing_lis = self.format.empty_listing()
            else:
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
                    self.filter_screen('Real Estate','real_estate')
                    self.format.preview_comment = f'Page {curr_page} of {len(self.page_list)} | Filter: [{self.filter_str}]'
                    self.format.comment = 'Select an option'

                elif input_int == 2: # Select house
                    self.format.comment = 'Enter ID of Real estate'
                    self.format.print_screen()
                    id_input = self.get_input('Input')
                    if id_input in id_list:
                        self.real_estate_profile_screen(id_input)
                        self.emp_list = self.inter.listing_all_real_estates()
                        id_list = []
                        [id_list.append(employee[1])for employee in self.emp_list]
                        # Make list for each screen again
                        self.page_list = self.screen_lists_from_all(self.emp_list)
                        self.filter_str = ''
                        curr_page = 1

                    else:
                        self.format.comment = 'ID not valid, Select an option'
                    self.format.preview_title = f'{"Address":<30} | {"ID":<5} | {"Address ID":<10} | {"Location":<12}'
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

                elif input_int == 5: # ADD realestate
                    self.add_real_estate_profile()
                    self.emp_list = self.inter.listing_all_real_estates()
                    id_list = []
                    [id_list.append(real_estate[1])for real_estate in self.emp_list]
                    # Make list for each screen
                    self.page_list = self.screen_lists_from_all(self.emp_list)

                elif input_int == 6: #Back (goes to back the the main menu)
                    self.format.listing_lis = self.format.empty_listing()
                    self.format.comment = 'Select an option'
                    return

    def add_real_estate_profile(self):
        self.format.subtitle = 'Menu > Real estates > Add real estate'
        self.format.edit_commands(['*Address','*Address ID','*Location','Apply Changes','Cancel'])
        self.format.apply_styles([0,0,0,1,1])
        list_of_comments = ['Enter address',"Enter address ID",'Enter location']
        self.format.preview_comment = 'Required fields marked with *'

        # Set new values to the original ones
        while True:
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            elif type_of_input == 1:
                if input_int == 3: #APPLY
                    
                    new_data_dict = {'address': self.format.commands['*Address'][1][1:-1],
                                    'real_estate_id': self.format.commands['*Address ID'][1][1:-1],
                                    'destination': self.format.commands['*Location'][1][1:-1]}
                    
                    if self.format.commands['*Address ID'][1][1:-1] == 'empty':
                        new_data_dict.pop('real_estate_id')
                
                    edit_response = self.inter.add_profile(self.role,'real_estate',new_data_dict)
                    if not edit_response:
                        if self.role == 'boss':
                            self.format.comment = 'Address id already registered, Select an option'
                        else:
                            self.format.comment = 'Unauthorized, Select an option'
                    else:
                        #UPDATE SCREEN

                        self.format.comment = 'Select an option'
                        return
                        

                elif input_int == 4: #Cancel
                    self.format.comment = 'Select an option'
                    return
            else:
                self.format.comment = list_of_comments[input_int]
                self.format.print_screen()
                input_str = self.get_input('Text input')
                self.format.update_text_box(input_int, input_str)
                self.format.comment = 'Select an option'
                

    def real_estate_profile_screen(self, id_str):
        self.format.comment = 'Select an option'
        self.format.profile = True
        while True:
            self.format.subtitle = 'Menu > Real Estate > Select'
            self.format.edit_commands(['Edit info','Back'])
            self.format.apply_styles([1,1])
            self.format.preview_title = 'Real estate information'
            self.format.listing_lis = self.inter.custom_real_estate_preview(id_str)
            self.format.preview_comment = ''
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            else:
                if input_int == 0: # Edit info
                    self.edit_real_estate_profile(id_str)

                elif input_int == 1: # Back
                    self.format.comment = 'Select an option'
                    self.format.profile = False
                    return

    def edit_real_estate_profile(self, id_str):
        self.format.subtitle = 'Menu > Real Estate > Select > Edit info'
        list_of_comments = ['Enter new address','Enter new location','Enter new address id','Enter new maintenance info']
        self.format.edit_commands(['Address','Location','Address ID','Maintenance','Apply Changes','Cancel'])
        self.format.apply_styles([0,0,0,0,1,1])

        estate_data_dict = self.inter.get_real_estate(id_str)

        # Sets new values to the original ones
        self.format.update_text_box(0,estate_data_dict['address'])
        self.format.update_text_box(1,estate_data_dict['destination'])
        self.format.update_text_box(2,estate_data_dict['real_estate_id'])
        self.format.update_text_box(3,estate_data_dict['maintenance_info'])     

        while True:
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            elif type_of_input == 1:
                if input_int == 4: # Apply changes

                    new_data_dict = {'id': estate_data_dict['id'], 
                                    'real_estate_id': self.format.commands['Address ID'][1][1:-1],  
                                    'address': self.format.commands['Address'][1][1:-1], 
                                    'destination': self.format.commands['Location'][1][1:-1], 
                                    'maintenance_info': self.format.commands['Maintenance'][1][1:-1]}

                    edit_response = self.inter.edit_profile(self.role, 'real_estate',new_data_dict)
                    if not edit_response:
                        self.format.comment = 'Unauthorized, Select an option'   
                    else:
                        self.format.listing_lis = self.inter.custom_real_estate_preview(new_data_dict['id'])
                        return
                        
                elif input_int == 5: # Cancel
                    self.format.comment = 'Select an option'
                    return
            else:
                self.format.comment = list_of_comments[input_int]
                self.format.print_screen()
                input_str = self.get_input('Text input')
                self.format.update_text_box(input_int, input_str)
                self.format.comment = 'Select an option'