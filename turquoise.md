# Turquoise

## Features

- [Infix notation](https://en.wikipedia.org/wiki/Infix_notation) for a variety of [mathematical operators](https://en.wikipedia.org/wiki/mathematical_operators)
- Shorthand functions for common operations and expressions
- Seamless integration of calculations involving numbers, symbols, strings, booleans, lists, and more

Several tools for debugging and development are also under development or planned:

- [Transpiling](https://en.wikipedia.org/wiki/Transpiling) to clean [Python](https://en.wikipedia.org/wiki/Python) code
- Interactive visualization of the [abstract syntax tree](https://en.wikipedia.org/wiki/abstract_syntax_tree) for use in debugging
- A [linter](https://en.wikipedia.org/wiki/linter) to standardize code written in Turquoise
- A [profiler](https://en.wikipedia.org/wiki/profiler) to analyze the performance of Turquoise programs
- [Time complexity](https://en.wikipedia.org/wiki/Time_complexity) and [space complexity](https://en.wikipedia.org/wiki/space_complexity) analysis of algorithms
- An interactive debugger

## Design Philosophy

### Brevity
Turquoise draws on the [object-oriented](https://en.wikipedia.org/wiki/object-oriented) principles of languages like Python and [JavaScript](https://en.wikipedia.org/wiki/JavaScript), but emphasizes concision to accelerate the development workflow.

### Flexibility
Turquoise's data structures and operators are structured to be infinitely reconfigurable to the needs of your task.

### Efficiency
A core part of Turquoise's design philosophy revolves around making the planning -> development -> feedback loop as seamless and pain-free as possible. The language is dynamic and meant to be interacted with as a key part of the development process.

### Interoperability
This is currently a (very) new and feature-limited programming language, so it is intended to work cohesively with other technologies, libraries, and modules while maintaining a reasonable dependency scope for the language's core features. Eventually, Turquoise will be able to run arbitrary Python code on representations of its data structures and likewise, snippets of Turquoise code will be able to be executed with a Python library. Transpiling (transcompiling) is also being explored as a way to bridge the gap between Turquoise's methodology and Python's massive ecosystem of modules and libraries.

### Intuitiveness
Everything in the language should, to a reasonable extent, do what you expect it to. When confusion arises, efficient strategies for clarifying the language's behavior will be available.

### Consistency
Exceptions to rules and principles should be minimized wherever possible in order to make the language's basic concepts universally applicable.

## Contributing

Turquoise is not accepting contributions at this time. If there is a feature you want considered for the language, please feel free to open a [new issue](https://github.com/generic-github-user/turquoise/issues/new/choose). Contributions of pull requests and specific functionality may be accepted in the future once the core features of the language have been built out and it is reasonably stable.
## Imports
Turquoise is designed to minimize the amount of essential functionality implemented in Python; and thus the number of external libraries included. A few standard modules are used for more convenient implementation of functions that mimic or extend those of Python.
### General
```python
import math
import string
import operator as ops
```
### Visualization
```python
import networkx as nx
from pyvis.network import Network
import matplotlib.pyplot as plt
```
### Miscellaneous
```python
import uuid
import itertools
```
## Range
Describes range expressions in Turquoise; these are similar to the Python version, but allow floating-point numbers for the start, stop, and step parameters. The syntax is `start:stop` or `start:stop:step`; if a step is not specified, the default will be 1.
```python
class Range:
    def __init__(self, start, stop=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = None
        self.result_type = Array
        self.report = ['start', 'stop', 'step']
        
    def evaluate(self):
#         self.value = list(range(self.start, self.stop+1, self.step))
        values = []
        num_steps = round((self.stop-self.start)/self.step)+1
        for i in range(num_steps):
            values.append(self.start+(self.step*i))
        self.value = Array(values)
        return self.value
```
## Tetration
```python
def tetration(n, m):
    r = n
#     m must be an integer
    m = int(m)
#     Repeatedly raise initial value to the previously computed power (e.g., 2 -> 2^2 -> 2^(2^2) -> ...)
    for i in range(m):
        r = n ** r
    return r
tetration.info = "This function handles Turquoise's tetration functionality, which uses the ^^ operator; it is generally impractical due to extremely rapid increases in the function's output as n and m grow, but is included for completeness."

tetration(1.6, 6)
```
## Expression
```python
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
            '!': ('math.factorial([](https://en.wikipedia.org/wiki/))', 'math'),
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
```
## Array
```python
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
```
```python
# a = [3,3,3]
# b = [4,4,4]
# a@b
```
```python
'-6'.isnumeric()
float('-6')
```
```python
bool([])
```
## Block
```python
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
#             print('[](https://en.wikipedia.org/wiki/)[](https://en.wikipedia.org/wiki/):[](https://en.wikipedia.org/wiki/)'.format(indent, k, v))
        if self.parsed:
            for k in self.parsed.report:
                v = getattr(self.parsed, k)
                print(indent*(level)+'[](https://en.wikipedia.org/wiki/)[](https://en.wikipedia.org/wiki/):[](https://en.wikipedia.org/wiki/)'.format(indent, k, str(v)))
        if self.report:
            for k in self.report:
                v = getattr(self, k)
                print(indent*(level)+'[](https://en.wikipedia.org/wiki/)[](https://en.wikipedia.org/wiki/):[](https://en.wikipedia.org/wiki/)'.format(indent, k, str(v)))
                
    def has_tokens(self):
        return any(type(b) is Token for b in self.children)
    
    def like(self, test):
        return self.type and (self.type == test or self.type.startswith(test))
        
    def __getitem__(self, i):
        return self.children[i]
    
    def __setitem__(self, i, j):
        self.children[i] = j
```
## Token
```python
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
```
```python
class Number:
    def __init__(self, a):
        self.a = float(a)
        
    def evaluate(self):
        return self.a
```
```python
class Group:
    def __init__(self, a):
        self.a = a
        self.value = self.a
        self.report = ['a']
    
    def evaluate(self):
        self.value = self.a
        return self.value
```
## Program
```python
class Program:
    def __init__(self, source):
        self.source = source
#         Create the root node
        self.tree = Block(block_type='root')
        
#         List of characters and their corresponding type
        self.char_sets = {
            'numeric': string.digits + '.-',
            'op': '!@#$%^&*/-+<>=?',
            'syntax': '()[][](https://en.wikipedia.org/wiki/),;:=|',
            'letter': string.ascii_lowercase
        }
#         List of syntactical patterns to match to generate the program's structure
#         i.e., the grammar
#         Patterns are listed from highest priority to lowest; a 3-parameter range (a:b:c) will be considered before a 2-parameter one (a:b)
        self.patterns = {
#             'range': ['numeric', ':', 'numeric']
#             'number': [
#                 lambda x: x[0].like('num'),
#                 lambda x: [x[0]],
#                 Number,
#                 1
#             ],
#             3-parameter range expression; start:stop:step
            'range1': [
                lambda x: x[0].like('num') and x[1].s == ':' and x[2].like('num') and x[3].s == ':' and x[4].like('num'),
                lambda x: [x[0], x[2], x[4]],
                Range,
                5
            ],
#             2-parameter range expression; start:stop (default step of 1 is used)
            'range2': [
#                 lambda x: [x[0].like('num') and x[1] == ':' and x[2].like('num')],
#                 lambda x: x[0].like('num') and x[1] == ':' and x[2].like('num'),
                lambda x: x[0].like('num') and x[1].s == ':' and x[2].like('num'),
                lambda x: [x[0], x[2]],
                Range,
                3
            ],
#             Factorial expression; 'number!'
            'factorial': [
                lambda x: x[0].like('num') and x[1].s == '!',
                lambda x: [x[0], None, x[1]],
                Expression,
                2
            ],
#             A mathematical expression using infix notation; 'a?b' or '3*5'
            'expression': [
                lambda x: x[0].like('num') and x[1].like('op') and x[2].like('num'),
                lambda x: [x[0], x[2], x[1]],
                Expression,
                3
            ],
            'group1': [
                lambda x: x[0].s == '[' and x[2].s == ']',
                lambda x: [x[1]],
                Group,
                3
            ],
        }
        
#         Run the lexer and parser
        self.lex()
        self.parse(self.tree)
        self.graph = None
        self.py_imports = [
            ['factorial', 'math']
        ]
    
    def traverse(self, block, callback):
        callback(block)
        for b in block.children:
            callback(b)
            if b.children:
                self.traverse(b, callback)
#             else:
#                 callback(b)
#                 return b
    
    def visualize(self):
#         Create a NetworkX graph representing the parse tree
#         self.graph = nx.DiGraph()
        self.graph = Network(width=800, height=800, notebook=True, directed=True)
#         Add nodes and edges for each block/relationship in the tree
        font = ['align': 'middle'](https://en.wikipedia.org/wiki/'align':_'middle')
        self.traverse(self.tree, lambda x: self.graph.add_node(x.id, label=(x.source if len(x.source) < 50 else ' '), font=font, shape='circle'))
        self.traverse(self.tree, lambda x: self.graph.add_edges([(x.id, y.id) for y in x.children]))
#         Generate and display the visualization
#         self.vis = Network(width=800, height=800, notebook=True)
        self.vis = self.graph
        self.vis.show_buttons()
#         self.vis.from_nx(self.graph)
        result = self.vis.show('parse_tree_visualization.html')
        return result
    
    def match_types(x, y):
        return all(xi.like(y[i]) for i, xi in enumerate(x))
    
    def char_type(self, x):
#         return list(filter(lambda x: k for k, v in self.char_sets if x in v))[0]
        return [k for k, v in self.char_sets.items() if x in v][0]
    
    def lex(self):
#         Both newlines and pipes, |, separate statements
        statements = self.source.replace('|', '\n').split('\n')
#         Remove empty lines
        statements = list(filter(None, statements))
#         Loop through lines in program
        for s in statements:
#             print(s)
            statement_parse = Block(block_type='section', source=s)
            token = Token(string=s[0], token_type=self.char_type(s[0]))
            for c in s[1:]:
                c_type = self.char_type(c)
#                 If character matches the type of the current token, append it
                if c_type == token.token_type:
                    token += c
#                 Otherwise, store the token and start a new one
                else:
                    statement_parse.add(token)
#                     print(token.string)
                    token = Token(c, token_type=c_type)
            statement_parse.add(token)
#             Add the parse for this line to the tree (top level)
            self.tree.add(statement_parse)
    
    def parse(self, block, level=0, max_level=5):
        if level <= max_level:
            for j, b in enumerate(block.children):
                self.parse(b, level=level+1, max_level=max_level)
#             i = 0
    #         Loop through stored patterns
            for k, v in self.patterns.items():
#                 Separate pattern list into the matching rule, resulting block, type of new block to be constructed, and number of terms in the expression
                pattern, result, block_type, num = v
                for i in range(len(block.children)):
        #             num = 3
                    section = block[i:i+num]
        #             r = lambda x: x[0].like('num') and x[1] == ':' and x[2].like('num')
        #             Check that section has at least enough terms to evaluate the rule (e.g., '3 + 4' has 3 terms)
                    if len(section) >= num:
        #                 print(list(map(str, section)), pattern(section), section[1].like('num'))
                        if pattern(section):
        #                     print(True, list(map(str, block[i:i+num])))
        #                     block[i:i+num] = Block(section, parser=block_type, r=result, block_type='numeric')
        #                     Replace sub-blocks or tokens with a single block
                            block[i:i+num] = [Block(section, parser=block_type, r=result, block_type='numeric')]
        #                     Update the block in case any more rules are applicable
                            self.parse(block, level=level+1, max_level=max_level)
                            break
        #                 use has_tokens?
                    
    def execute(self, node=None, print_output=True, display_source=True, **kwargs):
#         Default node is the root node
        if not node:
            node = self.tree
        
#         Loop through nodes in tree
#         for b in node:
        for b in node.children:
            if b.parser in [Range, Expression, Group]:
                b.parsed.evaluate()
                
                #                 print(b[0].source)
#                 if b.parser in [Expression]:
#                 if b.parsed:
#                 print(b.source)
                if print_output:
                    if display_source and b.source:
                        display_string = b.source + ' -> ' + str(b.parsed.value)
                    else:
                        display_string = b.parsed.value
                    print(display_string)
            elif type(b) is Token:
                if print_output:
                    if display_source and b.source:
                        display_string = b.source + ' -> ' + str(b.evaluate())
                    else:
                        display_string = b.evaluate()
                    print(display_string)
#             Recursively execute subnodes
            else:
#                 for v in b:
#                     self.execute()
                self.execute(node=b, print_output=print_output, **kwargs)
    
    def transpile(self, auto_print=True):
        translation = []
        successful = True
        missed = 0
        for i, block in enumerate(self.tree.c):
#         for block in self.tree.children:
#             if hasattr(block.parser, 'python'):
#             print(block[0].parser)
#             if type(block[0].parser) is Expression:
#                 print(True)
            if block[0].parser in [Expression]:
                t = block[0].parsed.python()
                if auto_print:
                    t = 'print([](https://en.wikipedia.org/wiki/))'.format(t)
                translation.append(t)
            else:
                translation.append('# Line [](https://en.wikipedia.org/wiki/) could not be converted'.format(i+1))
                successful = False
                missed += 1
#         if not successful:
        if missed:
            translation.insert(0, '\n# [](https://en.wikipedia.org/wiki/) lines could not be converted from Turquoise to Python and should be translated manually.\n'.format(missed))
        text = '\n'.join(translation)
        for a, b in self.py_imports:
            if a in text:
                translation.insert(0, 'import [](https://en.wikipedia.org/wiki/).[](https://en.wikipedia.org/wiki/)'.format(b, a))
        return '\n'.join(translation)

                    
    def print_tree(self):
        print('\n')
        self.tree.print()
    
```
## Testing
### Automated
```python
class Test:
    def __init__(self, test_args):
        self.test_args = test_args
        self.num = 0
        self.successful = 0
        
    def run(self, show=True):
        for test in itertools.product(*self.test_args):
            test_string = ''.join(map(str, test))
            try:
                test_program = Program(test_string)
                result = test_program.execute(print_output=False)
                self.successful += 1
            except Exception as ex:
                result = ex
            
            if show:
                print('Test line "[](https://en.wikipedia.org/wiki/)"; result: [](https://en.wikipedia.org/wiki/)'.format(test_string, result))
            self.num += 1
        s, n = self.successful, self.num
        print('[](https://en.wikipedia.org/wiki/) of [](https://en.wikipedia.org/wiki/) tests ([](https://en.wikipedia.org/wiki/)%) were successful ([](https://en.wikipedia.org/wiki/)/[](https://en.wikipedia.org/wiki/)% failed)'.format(s, n, round(s/n*100, 2), n-s, round((1-s/n)*100, 2)))

possible_ops = list('+-/*%^<>:&|') + ['**', '^^', '<=', '>=', '==', '!=', '//']
g = [0, 0.2, 0.5, 1, 22, 333, -5]
t = Test([g, possible_ops, g])
t.run(show=False)
```
### Manual
```python
tests = """
7
?2?
[5]
1:10%2==1
6:16:.5
8==7
5!=3
5!
8>5
9<=3
51%13
25%3
3**3**3
3^3^3
3:10**2
5:30
1:15**3
1:10*9
3:30:3
20:0:-1
1+2+3
8*9+2
5+10
8*3
20/4
932//7
5+8.3
2**8
2^8
2^^3
"""

M = Program(tests)
# M.execute()
# M.visualize()
# M.print_tree()
print(M.transpile())

# vars(M.tree[0].parsed)


# M.tree[0].components[1].like('op')
# M.tree[-1].parser#.components[1].token_type
# store statement and result for each line (?)
```
```python
__name__
```
```python
vars(M.tree.c[5])
```
```python
[(a.source, a.parser, a.string) for a in M.tree.c[4][0][0]]
# M.tree[0]
```
```python
M.tree[2][0].c
```
```python
list(range(20, 0, -1))
```
```python
# M.__dict__
# M.tree[0][1].type
```
```python
bool([False])
f = [3, 7, 2, 1, 8]
f[0:3]
```


*This document was generated from [`turquoise.ipynb`](https://nbviewer.jupyter.org/github/generic-github-user/turquoise/blob/master/turquoise.ipynb) at 2021-06-04 18:02:07*