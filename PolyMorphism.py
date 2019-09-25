class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    
    def display(self):
        print('Id: ', self.empid)
        print('Name: ', self.name)
        print('Salary: ', self.salary)


class Developer(Employee):
    def __init__(self, empid, name, salary, deskId, raise_sal = 1.3):
        self.deskId = deskId
        self.raise_sal = raise_sal
        Employee.__init__(self, empid, name, salary)

    def display(self):
        Employee.display(self)
        print('Desk ID: ', self.deskId)

    def increament(self):
        self.salary = self.salary * self.raise_sal


class Manager(Employee):
    def __init__(self, empid, name, salary, cabinId, raise_sal = 1.5):
        self.cabinId = cabinId
        self.raise_sal = raise_sal
        Employee.__init__(self, empid, name, salary)

    def display(self):
        Employee.display(self)
        print('Cabin ID: ', self.cabinId)

    def increament(self):
        self.salary = self.salary * self.raise_sal

class Company:
    def __init__(self, employees):
        self.employees = employees

    def show_all_employees(self):
        for emp in self.employees:
            emp.display()

    def raise_salary(self, emp):
        emp.increament()

    def add_employee(self, emp):
        self.employees.append(emp)

d1 = Developer(1, 'ABC', 5000, 101)
m1 = Manager(2, 'XYZ', 8000, 201)

# d1.display()
# m1.display()

list1 = [d1, m1]
com = Company(list1)
com.show_all_employees()

com.raise_salary(com.employees[1])
com.show_all_employees()