from UI.ScreensUI import ScreensUI

class MainUI:
    def __init__(self):
        self.isloggedin = False
        self.screen = ScreensUI()
        self.first_login = True

    def run(self):  
        while True:
            self.isloggedin = self.screen.login_screen(self.first_login)
            if not self.isloggedin:
                self.first_login = False
            while self.isloggedin:
                self.first_login = True
                self.isloggedin = self.screen.menu_screen()

    def debug(self):
        while True:
            self.screen.menu_screen()

    
if __name__ == "__main__":
    #MainUI().run() # Runs from login screen
    MainUI().debug() # Runs from menu screen
