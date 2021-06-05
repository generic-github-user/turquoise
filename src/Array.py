import operator as ops
class Array:
    def __init__(self, terms=[]):
        self.data = []
        for t in terms:
            if type(t) is list:
                self.data.append(array(t))
            else:
                if t not in list(',;'):
                    self.data.append(t)
    
    def apply(self, op, b, data=None):
        if not data:
            data = self.data
#         Make a new array to use as the function output
        result = Array()
        for d in data:
#             Recursively apply operation to nested arrays
            if type(d) is Array:
                result.append(self.apply(op, b, data=d))
#             Apply op directly to primitive types
            elif type(d) in [int, float]:
                result.append(op(d, b))
        return result
    
    def append(self, x):
        self.data.append(x)
    
#     Define magic operators so that operator module functions can be applied to Array instances (in the same way as native Python objects/primitive types)

#     Basic
    def __add__(self, b): return self.apply(ops.add, b)
    def __mul__(self, b): return self.apply(ops.mul, b)
    def __sub__(self, b): return self.apply(ops.sub, b)
#     Division
    def __truediv__(self, b): return self.apply(ops.truediv, b)
    def __floordiv__(self, b): return self.apply(ops.floordiv, b)
#     Other
    def __pow__(self, b): return self.apply(ops.pow, b)
    def __mod__(self, b): return self.apply(ops.mod, b)
#     Logical
    def __lt__(self, b): return self.apply(ops.lt, b)
    def __le__(self, b): return self.apply(ops.le, b)
    def __gt__(self, b): return self.apply(ops.gt, b)
    def __ge__(self, b): return self.apply(ops.ge, b)
#     Equality
    def __eq__(self, b): return self.apply(ops.eq, b)
    def __ne__(self, b): return self.apply(ops.ne, b)
#     Boolean
    def __and__(self, b): return self.apply(ops.and_, b)
    def __or__(self, b): return self.apply(ops.or_, b)
    
    def __str__(self):
        items = ', '.join(map(str, self.data))
        items = '['+items+']'
        return items