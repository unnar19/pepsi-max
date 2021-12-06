import os

class FormatUI:
    def __init__(self):
        '''
        FormatUI is a class used to format the information on-screen 
        such as commands, styles of inputs and preview and prints.
        '''
        self.title =            f'{"":<40}NaN-Air | Dividing by zero every day!'
        self.line =             '─'*120
        self.subtitle =         'Location in program'
        self.commands =         {'First command': [],'Second command': [],'Third command':[]}
        self.styles =           ['[empty]','','( )','(X)']
        self.comment =          'Select an option'
        self.prompt_str =       'Input'
        self.max_lines =        20
        self.preview_title =    ''
        self.preview_comment =  ''
        self.profile = False
        self.divider_loc =      50
        self.listing_lis = self.empty_listing()
        self.apply_styles([0,1,2])
        self.set_size_of_terminal()

    def reset_title(self):
        self.title = f'{"":<40}NaN-Air | Dividing by zero every day!'

    def empty_listing(self):
        empty_lis = []
        [empty_lis.append(['','','','']) for _ in range(self.max_lines)]
        return empty_lis

    def set_size_of_terminal(self):
        if os.name == 'nt':
            pass
            #os.system('mode 120,30')
        else:
            os.system('resize -s 120 30')

    def update_check_box(self, num):
        key_list = list(self.commands)
        if self.commands[key_list[num]][0] == 2:
            self.commands[key_list[num]][0] = 3
            self.commands[key_list[num]][1] = self.styles[3]
        elif self.commands[key_list[num]][0] == 3:
            self.commands[key_list[num]][0] = 2
            self.commands[key_list[num]][1] = self.styles[2]

    def update_text_box(self, num, some_str):
        '''
        Updates the text box, given the index and the input_str
        '''
        key_list = list(self.commands)
        if some_str == '':
            self.commands[key_list[num]][1] = '[empty]'
        else:
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
        top, mid, bottom, long, side, flat = '─','─','─',' ',' ',' '
        if self.preview_title:
            top, mid, bottom, long, side, flat = '┬','┼','┴','│','├','─'

        self.clear_screen()

        # Prints the header
        print()
        print(self.title)
        print(f'{self.line[:self.divider_loc]}{top}{self.line[self.divider_loc+1:]}')
        print(f' {self.subtitle:<47}{"":<2}{long} {self.preview_title}')
        print(f'{side:>51}{flat*69}')

        # Prints command row lines
        for index, key in enumerate(self.commands.keys()):
            extra = self.commands[key][1]
            if self.commands[key][0] == 0: # print shorter text box if neccesary
                if len(extra) > 21:
                    extra = extra[:17] + '...]'                             
            
            if self.profile:
                line_in_list = self.listing_lis[index][0]
            else:
                line_in_list = f'{self.listing_lis[index][0]:<30}   {self.listing_lis[index][1]:<5}   {self.listing_lis[index][2]:<10}   {self.listing_lis[index][3]:<12}'

            print(f'{index+1:>10}. {key:<15}{extra:<21}{"":<2}{long} {line_in_list}')

        # Prints the rows below the command rows
        for index in range(len(self.commands),self.max_lines):
            if self.profile:
                line_in_list = self.listing_lis[index][0]
            else:
                line_in_list = f'{self.listing_lis[index][0]:<30}   {self.listing_lis[index][1]:<5}   {self.listing_lis[index][2]:<10}   {self.listing_lis[index][3]:<12}'
            print(f'{long:>51} {line_in_list}')

        # Prints the footer
        print(f'{self.line[:self.divider_loc]}{mid}{self.line[self.divider_loc+1:]}')
        print(f' {self.comment:<47}{"":<2}{long} {self.preview_comment}')
        print(f'{self.line[:self.divider_loc]}{bottom}{self.line[self.divider_loc+1:]}')