from EmployeeUI import EmployeeUI
import os
#from Logic.LogicAPI import LogicAPI
#import json

class MainUI:
    def __init__(self):
        self.isloggedin = False
        self.emp = EmployeeUI()
    
        while (not self.isloggedin):
            self.isloggedin = self.emp.login_screen()
        while self.isloggedin:
            os.system('cls')
            print('main menu')
            break

if __name__ == "__main__":
    ass = MainUI()
