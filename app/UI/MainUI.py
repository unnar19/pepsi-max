import os

class MainUI:
    def __init__(self):
        self.isloggedin = False
        self.command_list = ['Email','Password','Log-in']
        self.view = ['[empty]','[empty]', '']
        self.hiddenformat = [1]
        self.length = len(self.command_list)
        self.location = 'Log-in'
        self.line = "------------------------------------------------------------------------------------------------------------------------"

    def header(self):
        return '{:<40}NaN Air | Dividing by zero every day!\n'.format('') + self.line

    def footer(self, comment_str):
        return self.line + "\n {}\n".format(comment_str) + self.line

    def getinput(self):
        return input(" Input: ")

    def changeView(self, index, some_str):
        if self.view[index] != '':
            if len(some_str) == 0:
                self.view[index] = '[empty]'
            else:
                if len(some_str) <= 25:
                    self.view[index] = '[{}]'.format(some_str)
                else:
                    self.view[index] = '[{}...]'.format(some_str[:25])

    def checkInput(self, input_str):
        if input_str == '1':
            return self.printScreen('Enter email address',editable=False, editing=1)
        elif input_str == '2':
            return self.printScreen('Enter password',editable=False, editing=2)
        elif input_str == '3':
            os.system('cls')
            print('Authenticate user, if exists log-in, else repeat')
        else:
            return self.printScreen()

    def hideString(self, input_str):
        hidden_str = ''
        for _ in range(len(input_str)):
            hidden_str += '*'
        return hidden_str

    def printScreen(self, comment_str='Please select an option',editable=True, editing=0):
        os.system('cls')
        print(self.header())
        print(" {}\n".format(self.location))
        for i in range(self.length):
            print("\t{}. {:<20} {}".format(str(i+1),self.command_list[i],self.view[i]))
        
        for i in range(self.length,21):
            print('')
        
        print(self.footer(comment_str))
        input_str = self.getinput()
        if editable:
            self.checkInput(input_str)
        else:
            if editing-1 in self.hiddenformat:
                input_str = self.hideString(input_str)
                self.changeView(editing-1, input_str)
            else:
                self.changeView(editing-1, input_str)
            return self.printScreen()

if __name__ == "__main__":
    some = MainUI()
    some.printScreen()