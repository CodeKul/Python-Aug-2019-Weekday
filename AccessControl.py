class MyClass:
    def __init__(self, a):
        self.__a = a

    def __display(self):
        print('Value of a: ',self.__a)

    def show_details(self):
        self.__display()

    def set_a(self, a):
        self.__a = a

obj1 = MyClass(100)
obj1.show_details()
obj1.__a = 200
obj1.show_details()
obj1.set_a(300)
obj1.show_details()