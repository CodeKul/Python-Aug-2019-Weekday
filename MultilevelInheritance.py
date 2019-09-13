class A:
    def __init__(self, a):
        self.a = a

    def display(self):
        print('a:', self.a)

class B(A):
    def __init__(self, a, b):
        self.b = b
        A.__init__(self, a)

    # def display(self):
    #     A.display(self)
    #     print('b:', self.b)

class C(B):
    def __init__(self, a, b, c):
        self.c = c
        B.__init__(self, a, b)

    # def display(self):
    #     B.display(self)
    #     print('c:', self.c)

objC = C(10, 20, 30)
objC.display()
