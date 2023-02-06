class A:
    def __init__(self, foo, bar, lorem):
        self.foo = foo
        self.bar = bar
        self.lorem = lorem

class B:
    def __init__(self):
        super(A, self).__init__()

class C:
    def __init__(self):
        super(A, self).__init__()