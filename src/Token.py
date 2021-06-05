import Block
import string
class Token(Block):
    def __init__(self, string='', token_type=None):
        super().__init__()
        self.string = string
        self.s = self.string
        self.token_type = token_type
        self.type = self.token_type
        self.report = ['string']
        if self.string:
            self.source = self.string
    
    def print(self, **kwargs):
        print(str(self))
    
    def evaluate(self):
        return self.string
    
    def __iadd__(self, x):
        self.string += x
        self.source = self.string
        self.s = self.string
        return self
    
    def __str__(self, **kwargs):
#         super().print(label='Token', **kwargs)
        return 'Token: '+self.string+': '+self.type