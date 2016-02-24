class fibonacci_sequence:
    def __init__(self, l):
        self.l = l
        self.a = 0
        self.b = 1
        self.f = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.f += 1
        if self.f > self.l:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return self.a