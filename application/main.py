from Employee import *

def employee_print():
    print("Employee Details:")
    empl.print()

def heppy_employee():
    empl.birthday()
    empl.print()

def employee_annual_salary():
    print("Employee annual salari: ", end="")
    print(f'{empl.annual_salary():.2f}')

def employee_raise_salary():
    percent = int(input("Entaer persent: "))
    empl.salarysalary = empl.rise_salary(percent)
    empl.print()

empl = None
e_id = ""
e_first_name = ""
e_last_name = ""
e_city = ""
e_street = ""
e_number = 0
e_age = 0
e_salary = 0.00

while True:
    print("Select:")
    print("1. Create new Employee")
    print("2. Show Employee details")
    print("3. Happy Birthday")
    print("4. Show Employee annual salary")
    print("5. Raise salary by persent")
    print("0. Exit Program")
    ans = int(input("Enter your choice: "))
    if ans == 0:
        print("Program exit!")
        break
    if ans == 1:
        e_id = input("Enter Employee ID: ")
        e_first_name = input("Enter Employee First Names: ")
        e_last_name = input("Enter Employee Last Names: ")
        e_city = input("Enter Employee City: ")
        e_street = input("Enter Employee Street: ")
        e_number = int(input("Enter Employee Street Number: "))
        e_age = int(input("Enter Employee Ages: "))
        e_salary = float(input("Enter Employee Salary: "))
        empl = Employee(e_first_name, e_last_name, e_city, e_street, e_number, e_age, e_id, e_salary)
        continue
    if ans == 2:
        employee_print()
        continue
    if ans == 3:
        heppy_employee()
        continue
    if ans == 4:
        employee_annual_salary()
        continue
    if ans == 5:
        employee_raise_salary()
