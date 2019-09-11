class A:

    def __init__(self, a):
        self.a = a
    
    def display(self):
        print('a:', self.a)

class B(A):
    def __init__(self, a, b):
        self.b = b
        A.__init__(self, a)

    def print_info(self):
        A.display(self)
        print('b:', self.b)

objB = B(10, 20)
objB.a = 100
objB.display()
objB.print_info()

objA = A(300)
objA.print_info()