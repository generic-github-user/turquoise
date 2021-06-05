import Array
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