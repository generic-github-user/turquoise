class Group:
    def __init__(self, a):
        self.a = a
        self.value = self.a
        self.report = ['a']
    
    def evaluate(self):
        self.value = self.a
        return self.value