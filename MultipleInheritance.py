class A:
    def __init__(self, a):
        self.a = a

    def display123(self):
        print('a:', self.a)

class B:
    def __init__(self, b):
        self.b = b

    def display123(self):
        print('b:', self.b)

class C(B, A):
    def __init__(self, a, b, c):
        self.c = c
        A.__init__(self, a)
        B.__init__(self, b)

    def display(self):
        A.display123(self)
        B.display123(self)
        print('c:', self.c)

objC = C(10, 20, 30)
objC.display()

# objA = A(100)
# objA.display()

# objB = B(200)
# objB.display()

# objC = objB
# objC.display()