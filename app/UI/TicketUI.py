from UI.FormatUI import FormatUI
from UI.InteractionsUI import InteractionsUI
from datetime import date

class TicketUI:
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

    def tickets_screen(self):  
        self.format.comment = 'Select an option'
        curr_page = 1
        self.filter_str = ''
        self.emp_list = self.inter.listing_all_for_destination('ticket',self.destination)
        id_list = []
        [id_list.append(ticket[1]) for ticket in self.emp_list]
        # Make list for each screen
        self.page_list = self.screen_lists_from_all(self.emp_list)

        while True:
            self.format.preview_title = f'{"Description":<30} | {"ID":<5} | {"Address ID":<10} | {"Closed":<12}'
            if self.filter_str == '':
                self.format.preview_comment = f'Page {curr_page} of {len(self.page_list)} | Filter: [empty]'
            self.format.subtitle = 'Menu > Tickets'
            self.format.edit_commands(['Filters','Select','Prev page','Next page','Add Ticket','Back'])
            self.format.apply_styles([1,1,1,1,1,1])

            if len(self.page_list) == 0:
                self.format.listing_lis = self.format.empty_listing()
            else:
                self.format.listing_lis = self.page_list[curr_page-1]

            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)

            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            elif type_of_input == 1: # Ticket Filters
                if input_int == 0:
                    self.filter_tickets_screen()
    
                elif input_int == 1: # Select Ticket
                    self.format.comment = 'Enter ID of ticket'
                    self.format.print_screen()
                    id_input = self.get_input('Input')
                    if id_input in id_list:
                        self.ticket_profile_screen(id_input)
                        self.emp_list = self.inter.listing_all_for_destination('ticket',self.destination)
                        id_list = []
                        [id_list.append(ticket[1])for ticket in self.emp_list]
                        # Make list for each screen again
                        self.page_list = self.screen_lists_from_all(self.emp_list)
                        self.filter_str = ''
                        curr_page = 1
                    else:
                        self.format.comment = 'ID not valid, Select an option'

                elif input_int == 2: # Previous page
                    if curr_page > 1:
                        self.format.comment = 'Select an option'
                        curr_page -= 1
                    else:
                        self.format.comment = 'Invalid input, Select an option'
                
                elif input_int == 3: # Next Page
                    if curr_page < len(self.page_list):
                        self.format.comment = 'Select an option'
                        curr_page += 1
                    else:
                        self.format.comment = 'Invalid input, Select an option'

                elif input_int == 4: # Add ticket
                    self.add_ticket_profile()
                    self.emp_list = self.inter.listing_all_for_destination('ticket',self.destination)
                    id_list = []
                    [id_list.append(ticket[1])for ticket in self.emp_list]
                    # Make list for each screen
                    self.page_list = self.screen_lists_from_all(self.emp_list)

                elif input_int == 5: # Back
                    self.format.listing_lis = self.format.empty_listing()
                    self.format.comment = 'Select an option'
                    return

    def filter_tickets_screen(self):
        self.format.subtitle = 'Menu > Tickets > Filters'
        self.format.edit_commands(['Show open','Employee ID','Address ID','Contrator ID','Clear'])
        self.format.apply_styles([1,1,1,1,1])

        # Filters: Filter all by location
        #   Show open
        #   Employee ID
        #   Address ID
        #   Contractor ID

        while True:
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            else:
                if input_int == 0: # Show open tickets
                    self.emp_list = self.inter.loc_and_extra_filter(self.destination, 'closed',False)
                    id_list = []
                    [id_list.append(ticket[1])for ticket in self.emp_list]
                    self.page_list = self.screen_lists_from_all(self.emp_list)
                    return

                elif input_int == 1: # Filter by employee id
                    self.format.comment = 'Enter employee ID'
                    self.format.print_screen()
                    input_str = self.get_input('Text input')
                    if input_str == '':
                        input_str == ' '
                    self.emp_list = self.inter.loc_and_extra_filter(self.destination, 'employee_id', input_str)
                    id_list = []
                    [id_list.append(ticket[1])for ticket in self.emp_list]
                    self.page_list = self.screen_lists_from_all(self.emp_list)
                    self.format.comment = 'Select an option'
                    return

                elif input_int == 2: # Filter by address id
                    self.format.comment = 'Enter address ID'
                    self.format.print_screen()
                    input_str = self.get_input('Text input')
                    if input_str == '':
                        input_str == ' '
                    self.emp_list = self.inter.loc_and_extra_filter(self.destination, 'real_estate_id', input_str)
                    id_list = []
                    [id_list.append(ticket[1])for ticket in self.emp_list]
                    self.page_list = self.screen_lists_from_all(self.emp_list)
                    self.format.comment = 'Select an option'
                    return

                elif input_int == 3: # Filter by contractor id
                    self.format.comment = 'Enter contractor ID'
                    self.format.print_screen()
                    input_str = self.get_input('Text input')
                    if input_str == '':
                        input_str == ' '
                    self.emp_list = self.inter.loc_and_extra_filter(self.destination, 'contractor_id', input_str)
                    id_list = []
                    [id_list.append(ticket[1])for ticket in self.emp_list]
                    self.page_list = self.screen_lists_from_all(self.emp_list)
                    self.format.comment = 'Select an option'
                    return

                else: # Back
                    self.format.comment = 'Select an option'
                    return

        
    def ticket_profile_screen(self, id_str):
        self.format.comment = 'Select an option'
        self.format.profile = True
        while True:
            self.format.subtitle = 'Menu > Tickets > Select'
            self.format.edit_commands(['Edit info','Add report','Back'])
            self.format.apply_styles([1,1,1])
            self.format.preview_title = 'Ticket information'
            self.format.listing_lis = self.inter.custom_ticket_preview(id_str)
            self.format.preview_comment = ''
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            else:
                if input_int == 0: # Edit info
                    self.edit_ticket_profile(id_str)

                elif input_int == 1: # Add report
                    ticket_data_dict = self.inter.get_ticket_or_report('ticket',id_str)
                    if ticket_data_dict['report_id'] == '0':
                        self.add_report_profile(id_str)
                    else:
                        self.format.comment = 'Ticket already has a report'

                elif input_int == 2: # Back
                    self.format.comment = 'Select an option'
                    self.format.profile = False
                    return

    def add_report_profile(self, ticket_id):
        self.format.subtitle = 'Menu > Tickets > Select > Add report'
        self.format.edit_commands(['*Description','Contractor ID','Contractor pay','Total cost','Accept','Cancel'])
        self.format.apply_styles([0,0,0,0,1,1])
        list_of_comments = ['Enter description','Enter contractor ID','Enter contractor pay','Enter total cost']
        self.format.preview_comment = 'Required fields marked with *'

        # Making a report
        #----------------
        # REQUIRED
        #   Description
        #   Address ID
        #   Employee ID
        #----------------
        # OPTIONAL
        #   total price
        #   contractor_id
        #   contractor_pay
    	#----------------
        # AUTOFILL
        #   destination = self.destination
        #   date = today
        #   ticket_id = ticket_id
        

        while True:            
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'

            elif type_of_input == 0: # Text box
                self.format.comment = list_of_comments[input_int]
                self.format.print_screen()
                input_str = self.get_input('Text input')
                self.format.update_text_box(input_int, input_str)
                self.format.comment = 'Select an option'
            
            elif type_of_input == 1: # Command
                if input_int == 4: #APPLY
                    today = str(date.today())

                    ticket_data_dict = self.inter.get_ticket_or_report('ticket',ticket_id)

                    # Make dictionary with new information
                    new_data_dict = {'date': today,
                                    'destination': self.destination,
                                    'ticket_id': ticket_id,
                                    'contractor_id': self.format.commands['Contractor ID'][1][1:-1],
                                    'contractor_pay': self.format.commands['Contractor pay'][1][1:-1],
                                    'total_price': self.format.commands['Total cost'][1][1:-1],
                                    'description': self.format.commands['*Description'][1][1:-1],
                                    'real_estate_id': ticket_data_dict['real_estate_id'],
                                    'employee_id': self.id}
                                    
                    # Remove optional fields to dictionary if they are empty
                    if self.format.commands['Contractor ID'][1][1:-1] == 'empty':
                        new_data_dict.pop('contractor_id')
                    if self.format.commands['Contractor pay'][1][1:-1] == 'empty':
                        new_data_dict.pop('contractor_pay')
                    if self.format.commands['Total cost'][1][1:-1] == 'empty':
                        new_data_dict.pop('total_price')


                    if new_data_dict['description'] == 'empty' or new_data_dict['real_estate_id'] == 'empty' or new_data_dict['employee_id'] == 'empty':
                        if self.role == 'boss':
                            self.format.comment = 'Required missing, Select an option'
                        else:
                            self.format.comment = 'Unauthorized, Select an option'
                    else:
                        self.inter.add_profile(self.role,'report',new_data_dict)
                        # Edit report id on ticket
                        
                        # TODO fix report/ticket id conflict

                        self.format.comment = 'Select an option'
                        return

                else: # Cancel
                    self.format.comment = 'Select an option'
                    return


    def edit_ticket_profile(self, id_str):

        ticket_data_dict = self.inter.get_ticket_or_report('ticket',id_str)
        prior = ticket_data_dict['priority']
        self.format.edit_commands(['Description','Address ID','Employee ID','Contractor ID','Priority','Ready','Recurring','Apply Changes','Cancel'])
        self.format.apply_styles([0,0,0,0,1,2,2,1,1])

        if self.str2bool(ticket_data_dict['ready']):
            self.format.update_check_box(5)
            ready_style = self.format.commands['Ready'][0]
        else:
            ready_style = 2
        if self.str2bool(ticket_data_dict['is_recurring']):
            self.format.update_check_box(6)
            recur_style = self.format.commands['Recurring'][0]
        else:
            recur_style = 2

        self.format.update_text_box(0,ticket_data_dict['description'])
        desc = ticket_data_dict['description']
        self.format.update_text_box(1,ticket_data_dict['real_estate_id'])
        real_id = ticket_data_dict['real_estate_id']
        self.format.update_text_box(2,ticket_data_dict['employee_id'])
        emp_id = ticket_data_dict['employee_id']
        self.format.update_text_box(3,ticket_data_dict['contractor_id'])
        cont_id = ticket_data_dict['contractor_id']
        
        while True:
            self.format.edit_commands(['Description','Address ID','Employee ID','Contractor ID','Priority','Ready','Recurring','Apply Changes','Cancel'])
            self.format.apply_styles([0,0,0,0,1,ready_style,recur_style,1,1])
            self.format.subtitle = 'Menu > Tickets > Select > Edit info'
            list_of_comments = ['Enter new description','Enter new address ID','Enter new Employee ID','Enter new contractor ID','Edit priority']
            
            self.format.update_text_box(0,desc)
            self.format.update_text_box(1,real_id)
            self.format.update_text_box(2,emp_id)
            self.format.update_text_box(3,cont_id)

            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            elif type_of_input == 0: #Text box
                self.format.comment = list_of_comments[input_int]
                self.format.print_screen()
                input_str = self.get_input('Text input')
                self.format.update_text_box(input_int, input_str)
                if input_int == 0:
                    desc = input_str
                elif input_int == 1:
                    real_id = input_str
                elif input_int == 2:
                    emp_id = input_str
                elif input_int == 3:
                    cont_id = input_str
                self.format.comment = 'Select an option'
            elif type_of_input == 2 or type_of_input == 3:
                self.format.update_check_box(input_int)
                if input_int == 5:
                    ready_style = self.format.commands['Ready'][0]
                elif input_int == 6:
                    recur_style = self.format.commands['Recurring'][0]
            elif type_of_input == 1:
                if input_int == 4: # Priority
                    prior = self.ticket_priority_screen('Select > Edit info > Priority')
                    self.format.comment = 'Select an option'

                elif input_int == 7: # APPLY
                    ready = False
                    if self.format.commands['Ready'][0] == 3:
                        ready = True
                    recur = False
                    if self.format.commands['Recurring'][0] == 3:
                        recur = True

                    new_data_dict = {'id': ticket_data_dict['id'], 
                                    'description': self.format.commands['Description'][1][1:-1],  
                                    'real_estate_id': self.format.commands['Address ID'][1][1:-1],
                                    'employee_id': self.format.commands['Employee ID'][1][1:-1],
                                    'contractor_id': self.format.commands['Address ID'][1][1:-1],
                                    'priority': prior,
                                    'ready': ready,
                                    'is_recurring': recur}


                    edit_response = self.inter.edit_profile(self.role, 'ticket',new_data_dict)
                    if not edit_response:
                        self.format.comment = 'Unauthorized, Select an option'   
                    else:
                        self.format.listing_lis = self.inter.custom_ticket_preview(new_data_dict['id'])
                        return
    
                else: # Cancel
                    self.format.comment = 'Select an option'
                    return

    def ticket_priority_screen(self,location_in_program) -> str:
        self.format.comment = 'Select an option'
        while True:
            self.format.subtitle = f'Menu > Tickets > {location_in_program}'
            self.format.edit_commands(['Emergency','Now','ASAP','Clear'])
            priority_list = ['Emergency','Now','ASAP','']
            self.format.apply_styles([1,1,1,1])
            self.format.preview_title = 'Ticket information'
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'
            else:
                self.format.comment = 'Select an option'
                return priority_list[input_int]

    def add_ticket_profile(self):
        prior = ''
        ticket_data_list = ['empty']*3
        self.format.edit_commands(['*Description','*Address ID','Contractor ID','Priority','Recurring','Accept','Cancel'])
        self.format.apply_styles([0,0,0,1,2,1,1])
        recur_style = 2
        list_of_comments = ['Enter description','Enter address ID','Enter contractor ID']
        self.format.preview_comment = 'Required fields marked with *'

        while True:
            self.format.subtitle = 'Menu > Tickets > Add ticket'
            self.format.edit_commands(['*Description','*Address ID','Contractor ID','Priority','Recurring','Accept','Cancel'])
            self.format.apply_styles([0,0,0,1,recur_style,1,1])

            self.format.update_text_box(0,ticket_data_list[0])
            self.format.update_text_box(1,ticket_data_list[1])
            self.format.update_text_box(2,ticket_data_list[2])
            
            self.format.print_screen()
            input_str = self.get_input('Input')
            input_int, type_of_input = self.check_type_of_input(input_str)
            if type(type_of_input) != int:
                self.format.comment = f'{type_of_input}, Select an option'

            elif type_of_input == 0: # Text box
                self.format.comment = list_of_comments[input_int]
                self.format.print_screen()
                input_str = self.get_input('Text input')
                self.format.update_text_box(input_int, input_str)
                ticket_data_list[input_int] = input_str
                self.format.comment = 'Select an option'
            
            elif type_of_input == 1: # Command
                if input_int == 3: # priority screen
                    prior = self.ticket_priority_screen('Add ticket > Priority')
                    self.format.comment = 'Select an option'
                elif input_int == 5: #APPLY
                    today = str(date.today())

                    # Make dictionary with new information
                    new_data_dict = {'description': self.format.commands['*Description'][1][1:-1],
                                    'start_date': today,
                                    'contractor_id': self.format.commands['Contractor ID'][1][1:-1],
                                    'real_estate_id': self.format.commands['*Address ID'][1][1:-1],
                                    'employee_id': self.id,
                                    'destination': self.destination,
                                    'priority': prior}

                    # Add non required fields to dictionary if they are not empty
                    if self.format.commands['Contractor ID'][1][1:-1] == 'empty':
                        new_data_dict.pop('contractor_id')

                    if self.format.commands['Recurring'][0] == 3:
                        new_data_dict['is_recurring'] = True

                    if new_data_dict['description'] == 'empty' or new_data_dict['real_estate_id'] == 'empty' or new_data_dict['employee_id'] == 'empty':
                        if self.role == 'boss':
                            self.format.comment = 'Required missing, Select an option'
                        else:
                            self.format.comment = 'Unauthorized, Select an option'
                    else:
                        self.inter.add_profile(self.role,'ticket',new_data_dict)
                        self.format.comment = 'Select an option'
                        return

                else: # Cancel
                    self.format.comment = 'Select an option'
                    return
            
            else:
                self.format.update_check_box(input_int)
                recur_style = self.format.commands['Recurring'][0]