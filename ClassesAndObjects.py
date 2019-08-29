class MyClass:
    
    # Default initialiser
    # def __init__(self):
    #     self.myVar = 0

    # Parameterised initialiser
    # def __init__(self, myVar):
    #     self.myVar = myVar

    # copy initialiser
    def __init__(self, obj):
        print('init')
        if obj != None:
            self.myVar = obj.myVar
        else:
            self.myVar = 0

    def display(self):
        print('Value of myVar:', self.myVar)

    def setMyVar(self, myVar):
        self.myVar = myVar

myObj = MyClass(None)
myObj.myVar = 100
myObj.display()

myAnotherObj = MyClass(myObj)
myAnotherObj.display()
myAnotherObj.setMyVar(200)
myAnotherObj.display()