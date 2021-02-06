from Person import *

class Employee(Person):
    id = 0
    salary = 0.00
    def __init__(self, first_name, last_name, address_city, address_street, address_number, age, id, salary):
        self.id = id
        self.salary = salary
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = Address(address_city, address_street, address_number)
    def annual_salary(self):
        return self.salary*12
    def rise_salary(self, percent):
        self.salary = self.salary*(1+percent/100.00)
        return self.salary
    def print(self):
        print("ID Nimber: "+self.id+"; Employee name: "+self.full_name()+"; Age: "+str(self.age))
        print("Address: "+self.get_address())
        print("Salary: ", end="")
        print(f'{self.salary:.2f}')
