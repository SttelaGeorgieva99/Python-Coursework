from Address import *

class Person:
    first_name = "No First Name"
    last_name = "No Last Name"
    address = None
    age = 0
    def __init__(self, first_name, last_name, address_city, address_street, address_number, age):
        self.first_name = first_name
        self.last_name = last_name
        self.address = Address(address_city, address_street, address_number)
        self.age = age
    def full_name(self):
        return self.last_name+", "+self.first_name	
    def get_address(self):
        return self.address.city+" "+self.address.street+" "+str(self.address.number)
    def birthday(self):
        self.age += 1
        print("Happy Birthday "+self.full_name()+"!")
    def print(self):
        print(self.full_name()+" ", end="")
        self.get_address()
        print(" "+str(self.age))
