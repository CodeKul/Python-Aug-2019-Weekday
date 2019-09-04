# write a class and add a and b as member variables(operands), add set_operand() member function, also add addition, subtraction, multiplication, division as member functions.

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def setOperands(self, a, b):
        self.a = a
        self.b = b

    def displayOperands(self):
        print('a: {}\nb: {}'.format(self.a, self.b))

    def addition(self):
        res = self.a + self.b
        return res
    
    def subtraction(self):
        res = self.a - self.b
        return res

    def multiplication(self):
        res = self.a * self.b
        return res

    def division(self):
        res = self.a / self.b
        return res


calc = Calculator(10, 20)
calc.displayOperands()

res = calc.addition()

print('Result: ', res)