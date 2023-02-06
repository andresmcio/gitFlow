class A:
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar

class B:
    def __init__(self):
        super(A, self).__init__()