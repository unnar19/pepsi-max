from InteractionsUI import InteractionsUI

class EmployeeUI:
    def __init__(self) -> None:
        self.screen = InteractionsUI()

    def login_screen(self):
        self.screen.format.subtitle = 'Log-in Screen'
        self.screen.format.edit_commands(['Email','Password','Log-in'])
        self.screen.format.apply_styles([0,0,1])
        self.screen.format.print_screen()
        swag = self.screen.get_input('Select')
        return swag