import Token
import Block
import Expression
import Group
import Number
import Range
import networkx as nx
import string
import math
class Program:
    def __init__(self, source):
        self.source = source
#         Create the root node
        self.tree = Block(block_type='root')
        
#         List of characters and their corresponding type
        self.char_sets = {
            'numeric': string.digits + '.-',
            'op': '!@#$%^&*/-+<>=?',
            'syntax': '()[]{},;:=|',
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
        font = {'align': 'middle'}
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
                    t = 'print({})'.format(t)
                translation.append(t)
            else:
                translation.append('# Line {} could not be converted'.format(i+1))
                successful = False
                missed += 1
#         if not successful:
        if missed:
            translation.insert(0, '\n# {} lines could not be converted from Turquoise to Python and should be translated manually.\n'.format(missed))
        text = '\n'.join(translation)
        for a, b in self.py_imports:
            if a in text:
                translation.insert(0, 'import {}.{}'.format(b, a))
        return '\n'.join(translation)

                    
    def print_tree(self):
        print('\n')
        self.tree.print()
    