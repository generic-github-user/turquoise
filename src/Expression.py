import tetration
import operator as ops
import string
import math
class Expression:
    def __init__(self, a=None, b=None, op=None):
        self.a, self.b = a, b
        if type(a) is str:
            self.a = float(a)
        if type(b) is str:
            self.b = float(b)
        self.op = op
        self.op_list = {
            '+': ops.add,
            '*': ops.mul,
            '-': ops.sub,
            '/': ops.truediv,
            '//': ops.floordiv,
            '**': ops.pow,
            '^': ops.pow,
            '^^': tetration,
            '%': ops.mod,
            '!': math.factorial,
            '<': ops.lt,
            '<=': ops.le,
            '>': ops.gt,
            '>=': ops.ge,
            '==': ops.eq,
            '!=': ops.ne,
            '&': ops.and_,
            '|': ops.or_
        }
        self.report = ['a', 'op', 'b']
        self.python_ops = {
            '!': ('math.factorial({})', 'math'),
            '^': ('**', None)
        }
        
    def evaluate(self):
        op_name = self.op_list[self.op]
        self.value = op_name(self.a) if self.op in '!' else op_name(self.a, self.b)
        return self.value
    
    def python(self, spacing=1):
        o = self.python_ops[self.op] if self.op in self.python_ops else self.op
        if self.a and self.b:
            strings = map(str, [self.a, o[0], self.b])
            return (' '*spacing).join(strings)
        else:
            return o[0].format(self.a)
    
e1 = Expression('8', '6', '+')
e2 = Expression('5', None, '!')
e3 = Expression('9', '3', '^')
[e.python() for e in [e1, e2, e3]]