class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        print('({} + {}i)'.format(self.real, self.imag))

    def addition(self, c1):
        cn = ComplexNumber(0, 0)
        cn.real = self.real + c1.real
        cn.imag = self.imag + c1.imag
        return cn

    def subtraction(self, c1):
        cn = ComplexNumber(0, 0)
        cn.real = self.real - c1.real
        cn.imag = self.imag - c1.imag
        return cn

    def multiplication(self, c1):
        cn = ComplexNumber(0, 0)
        cn.real = self.real*c1.real - self.imag*c1.imag
        cn.imag = self.real*c1.imag + self.imag*c1.real
        return cn


com1 = ComplexNumber(5, 10)
com2 = ComplexNumber(2, 3)

com1.display()
com2.display()

com3 = com1.addition(com2)
com3.display()

com3 = com1.subtraction(com2)
com3.display()

com3 = com1.multiplication(com2)
com3.display()

com4 = complex(1, 2)
com5 = complex(2,3)
print(com4 + com5)