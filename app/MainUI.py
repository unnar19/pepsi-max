from UI.MenuUI import MenuUI

class MainUI:
    '''
    Contains the main loop of the program
    '''
    def __init__(self):
        self.isloggedin = False
        self.screen = MenuUI()
        self.first_login = True

    def run(self):
        '''
        Runs the program from the login screen
        '''
        while True:
            self.isloggedin = self.screen.login_screen(self.first_login)
            if not self.isloggedin:
                self.first_login = False
            while self.isloggedin:
                self.first_login = True
                self.isloggedin = self.screen.menu_screen()

    def debug(self):
        '''
        Runs the program from the menu, used to debug
        '''
        while True:
            self.screen.menu_screen()

    
if __name__ == "__main__":
    #MainUI().run() 
    MainUI().debug()