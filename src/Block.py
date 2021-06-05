import Token
import uuid
import string
class Block:
    def __init__(self, children=None, parsed=None, parser=None, r=None, block_type=None, source=''):
#         self.components = components
        self.parser = parser
        self.dtype = None
        self.block_type = block_type
        self.type = block_type
        self.report = []
        self.source = source
        self.string = ''
        self.s = self.string
        self.id = uuid.uuid4().hex
        
        self.children = children if children else []
        self.c = self.children
#         self.children = []
        
        self.parsed = None
        if self.children:
            comp_vals = []
            for q in self.children:
                if type(q) in [Token]:
                    q = q.string
                    
                if type(q) in [Block]:
                    if q.like('num'):
#                         q = int(q)
                        q = q.evaluate()
                
                if type(q) is str and self.numeric(q):
                    q = float(q)
                comp_vals.append(q)
            self.parsed = parser(*r(comp_vals))
            
            if not self.source:
                self.source = ''.join([b.source for b in self.children])

    def update(self):
        self.source = ''.join([b.source for b in self.children])
        return self

    def numeric(self, n):
        return all(c in (string.digits + '.-') for c in n)
            
    def add(self, x):
        self.children.append(x)
        self.update()
#         self.source += x.source
    
    def evaluate(self):
        return self.parsed.evaluate()
    
    def print(self, level=0, label='Block'):
        indent = ' '*2
#         print(self.type)
#         print(indent + str(self) + '; ' + type(self.parsed).__name__ + '; ' + str(self.type))
        print(indent*level + label + ': ' + type(self.parsed).__name__ + '; ' + str(self.type))
        for c in self.children:
            c.print(level=level+1)
#         for k, v in vars(self.parser).items():
#             print('{}{}:{}'.format(indent, k, v))
        if self.parsed:
            for k in self.parsed.report:
                v = getattr(self.parsed, k)
                print(indent*(level)+'{}{}:{}'.format(indent, k, str(v)))
        if self.report:
            for k in self.report:
                v = getattr(self, k)
                print(indent*(level)+'{}{}:{}'.format(indent, k, str(v)))
                
    def has_tokens(self):
        return any(type(b) is Token for b in self.children)
    
    def like(self, test):
        return self.type and (self.type == test or self.type.startswith(test))
        
    def __getitem__(self, i):
        return self.children[i]
    
    def __setitem__(self, i, j):
        self.children[i] = j