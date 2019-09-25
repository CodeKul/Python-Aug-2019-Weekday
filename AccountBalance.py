class Account:

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def display(self):
        print('Account info')
        print('Name:', self.name)
        print('Account no:', self.acc_no)
        print('Balance:', self.__balance)

    def deposite(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        self.__balance -= amt

acc1 = Account('ABC', 123456, 1000)
acc1.display()

acc1.deposite(100)

acc1.display()
acc1.__balance = 1200

acc1.display()

