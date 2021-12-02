from UI.EmployeeUI import EmployeeUI
from UI.InteractionsUI import InteractionsUI

class MainUI:
    def __init__(self):
        self.isloggedin = False
        self.emp = EmployeeUI()
        first_login = True
        
        while True:
            
            self.isloggedin, self.id, self.role, self.name = self.emp.login_screen(first_login)
            if not self.isloggedin:
                first_login = False
            while self.isloggedin:
                # Make menu screen
                first_login = True
                self.isloggedin = self.menu_screen()
                
    
    def menu_screen(self):
        screen = InteractionsUI()
        logged_str = f'Logged in as: {self.name}'
        screen.format.title += f'{logged_str:>42}'
        screen.format.edit_commands(['Employees','Real Estate','Maintenance','Contractors','Log-out'])
        screen.format.apply_styles([1,1,1,1,1])
        screen.format.print_screen()
        input_str = screen.get_input('Input')
        input_int, type_of_input = screen.check_type_of_input(input_str)
        if input_int == 0: #employees
            print('Employee screen')
            input('continue?')
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

if __name__ == "__main__":
    ass = MainUI()
