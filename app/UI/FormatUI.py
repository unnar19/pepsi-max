import os

class FormatUI:
    def __init__(self):
        '''
        FormatUI is a class used to format the information on-screen 
        such as commands, styles of inputs and preview.
        '''
        self.title =            'NaN-Air | Dividing by zero every day!'
        self.line =             '─'*120
        self.subtitle =         'Location in program'
        self.commands =         {'First command': [],'Second command': [],'Third command':[]}
        self.styles =           ['[empty]','','( )','(X)']
        self.comment =          'Select an option'
        self.prompt_str =       'Input'
        self.max_lines =        20
        self.preview_title =    ''
        self.preview_comment =  ''
        self.divider_loc =      50
        self.apply_styles([0,1,2])
        self.set_size_of_terminal()

    def set_size_of_terminal(self):
        if os.name == 'nt':
            pass
            #os.system('mode 120,30')
        else:
            os.system('resize -s 120 30')

    def change_text_box(self, num, some_str):
        key_list = list(self.commands)
        self.commands[key_list[num]][1] = f'[{some_str}]'

    def edit_commands(self, new_commands):
        '''
        Changes the commands available to the user
        '''
        self.commands = {}
        for c in new_commands:
            self.commands[c] = []
        return self.commands

    def apply_styles(self, style_list):
        '''
        Changes the style of input such as text input and check boxes
        '''
        for i, key in enumerate(self.commands.keys()):
            self.commands[key] = []
            self.commands[key].append(style_list[i])
            self.commands[key].append(self.styles[style_list[i]])
        return style_list
    
    def edit_comment(self, new_comment):
        '''
        Changes the comment above the input to give feedback to user
        '''
        self.comment = new_comment
        return self.comment

    def clear_screen(self):
        '''
        Clears the screen with commands depending on OS
        '''
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def print_screen(self):
        '''
        Prints the screen with the information provided to the class
        '''
        top, mid, bottom, long, side, flat = '─','─','─','','',''
        if self.preview_title:
            top, mid, bottom, long, side, flat = '┬','┼','┴','│','├','─'

        self.clear_screen()

        # Prints the header
        print()
        print(f'{self.title:>79}')
        print(f'{self.line[:self.divider_loc]}{top}{self.line[self.divider_loc+1:]}')
        print(f' {self.subtitle:<47}{"":<2}{long} {self.preview_title}')
        print(f'{side:>51}{flat*69}')

        # Prints command row lines
        for index, key in enumerate(self.commands.keys()):
            print(f'{index+1:>10}. {key:<15}{self.commands[key][1]:<21}{"":<2}{long}')

        # Prints the rows below the command rows
        for _ in range(len(self.commands),self.max_lines):
            print(f'{long:>51}')

        # Prints the footer
        print(f'{self.line[:self.divider_loc]}{mid}{self.line[self.divider_loc+1:]}')
        print(f' {self.comment:<47}{"":<2}{long} {self.preview_comment}')
        print(f'{self.line[:self.divider_loc]}{bottom}{self.line[self.divider_loc+1:]}')

if __name__ == "__main__":
    # Making the log-in screen to test
    login_screen = FormatUI()
    while True:  
        login_screen.subtitle = 'Log-in screen'
        login_screen.edit_commands(['Email','Password','Log-in'])
        login_screen.apply_styles([0,0,1])
        login_screen.preview_title = 'Preview header'
        login_screen.preview_comment = 'Preview footer'

        login_screen.print_screen()
        #login_screen.change_text_box(int(ret),'nice')
        #login_screen.print_screen()
        break
        
    