from UI.InteractionsUI import InteractionsUI

class ListUI:
    def __init__(self):
        self.screen = InteractionsUI()
    
    def employees_screen(self, id, role, name):        
        logged_str = f'Logged in as: {name}'
        self.screen.format.title += f'{logged_str:>42}'
        self.screen.format.subtitle = 'Menu > Employees'
        self.screen.format.edit_commands(['Search','Filters','Select employee','Next page','Previous page','Back'])
        self.screen.format.apply_styles([0,1,1,1,1,1])
        self.screen.format.preview_title = 'Name'
        self.screen.format.preview_comment = 'Page 1 of 1 | Filters: [all] HARDCODED'

        self.screen.format.print_screen()
        input_str = self.screen.get_input('Input')