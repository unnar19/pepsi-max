from FormatUI import FormatUI

class InteractionsUI:
    def __init__(self):
        self.format = FormatUI()

    def some(self):
        
        pass

    def get_input(self, prompt_str):
        return input(f' {prompt_str}: ')
