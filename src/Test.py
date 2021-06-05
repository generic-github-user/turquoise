import Program
import operator as ops
import string
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
                print('Test line "{}"; result: {}'.format(test_string, result))
            self.num += 1
        s, n = self.successful, self.num
        print('{} of {} tests ({}%) were successful ({}/{}% failed)'.format(s, n, round(s/n*100, 2), n-s, round((1-s/n)*100, 2)))

possible_ops = list('+-/*%^<>:&|') + ['**', '^^', '<=', '>=', '==', '!=', '//']
g = [0, 0.2, 0.5, 1, 22, 333, -5]
t = Test([g, possible_ops, g])
t.run(show=False)