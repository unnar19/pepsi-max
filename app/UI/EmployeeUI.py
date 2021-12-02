from InteractionsUI import InteractionsUI

class EmployeeUI:
    def __init__(self) -> None:
        self.screen = InteractionsUI()

    def login_screen(self):
        self.screen.format.subtitle = 'Log-in Screen'
        self.screen.format.edit_commands(['Email','Password','Log-in'])
        list_of_comments = ['Enter email address', 'Enter password'] 
        self.screen.format.apply_styles([0,0,1])
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
                return True 
                #TODO authenticate the user

            if not str(type_of_input).isdigit():
                self.screen.format.comment = f'{type_of_input}, Select an option'
            else:
                self.screen.format.comment = 'Select an option'


