from FormatUI import FormatUI
from Logic.LogicAPI import LogicAPI

class MainUI:
    def __init__(self):
        self.isloggedin = False
        self.format = FormatUI()

    def make_login_screen(self):
        self.format.subtitle = 'Log-in screen'
        self.format.edit_commands(['Email','Password','Log-in'])
        self.format.apply_styles([0,0,1])
        self.footers = []
        
if __name__ == "__main__":
    list_of_comments = ['Enter email address', 'Enter password']
    main = MainUI()
    main.make_login_screen()
    while not main.isloggedin:
        main.format.edit_comment('Select an option')
        main.format.print_screen()
        selection = main.format.get_input('Input')
        if selection == '1' or selection == '2': # Text box
            main.format.edit_comment(list_of_comments[int(selection)-1])
            main.format.print_screen()
            text = main.format.get_input('Text input')
            main.format.change_text_box(int(selection),text)
            main.format.print_screen()
        if selection == '3':
            LogicAPI.authenticate_employee()
            main.isloggedin = True
    main.format.clear_screen()
    print('authenticate the user')