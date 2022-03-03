from datetime import datetime

class NoSuchDepartmentExeption(Exception):
    pass

class Employee:
    'fname, lname, employmentdate, salary, department'
    counter = 0

    def __init__(self,fname,lname,employmentdate,salary,department):
        self.fname : str = fname
        self.lname : str = lname
        self.employeeid: int = Employee.counter
        self.employmentdate : str = employmentdate
        self.salary : int = salary

        if department in ["IT", "Accounting", "HR"]:
            self.department : str = department
        else:
            print("Department does not exist!!")
            raise NoSuchDepartmentExeption

        Employee.counter += 1

    def set_fname(self, fname):
        self.fname = fname

    def set_lname(self, lname):
        self.lname = lname

    def set_employeeid(self, employeeid):
        self.employeeid = employeeid

    def set_employmentdate(self, employmentdate):
        self.employmentdate = employmentdate

    def set_salary(self, salary):
        self.salary = salary

    def set_department(self, department):
        self.department = department


    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_employeeid(self):
        return self.employeeid

    def get_employmentdate(self):
        return self.employmentdate

    def get_salary(self):
        return self.salary

    def get_department(self):
        return self.department

# Create two employees
Emp_Ugonna = Employee('Ugonna', 'Onyekachi', '2022-02-15', 50000, 'IT')

Emp_Chi = Employee('Chi', 'Onyekachi', '2022-02-19', 60000, 'Accounting')




list_of_emps = [Emp_Ugonna, Emp_Chi]

# for emp in list_of_emps:
#     print(emp.get_fname())
#     print(emp.get_employeeid())
#
# print('-------------------------------------------------------------------------')
# print([(emp.get_employeeid(), emp.get_fname()) for emp in list_of_emps])
#
# print('-------------------------------------------------------------------------')
# # Test NoSuchDepartmentExeption
# Emp_Udo = Employee("Udo", "Onyeka", '2020-09-01', 100000, 'PE')



option = input("""What do yo want to do ?
Create Employee - C
Read/List Employee info - R
Update Employee info - U
Delete/Remove Employee - D
    Enter option: """)

print('\n------------------------------------------')
if option.strip().upper() == 'C':
    fname = input("What is the first name of the employee: ")
    lname = input("What is the last name of the employee: ")
    employmentdate = input("What is the employment date of the employee: ")
    salary = input("What is the salary of the employee: ")
    department = input("What department does this employee belong to: ")

    new_Emp = Employee(fname, lname, employmentdate, salary, department)
    list_of_emps.append(new_Emp)

    print([(emp.get_employeeid(), emp.get_fname()) for emp in list_of_emps])

elif option.strip().upper() == 'R':
    emp_id = input("What is the employee ID of the Employee you want to view their information? ")

    for emp in list_of_emps:
        if int(emp_id) == emp.get_employeeid():
            print("----------------EMPLOYEE INFO-----------------")
            print(f"Employee ID: {emp.get_employeeid()}")
            print(f"First Name: {emp.get_fname()}")
            print(f"Last Name: {emp.get_lname()}")
            print(f"Hire Date: {emp.get_employmentdate()}")
            print(f"Salary: ${emp.get_salary():,.2f}")
            print(f"Department: {emp.get_department()}")
            print("-----------------------------------------------")
            break
    else:
        print(f"Employee with ID = {emp_id} does not exist!!")

elif option.strip().upper() == 'U':
    emp_id = input("What is the employee ID of the Employee you want to update their information? ")

    for emp in list_of_emps:
        if int(emp_id) == emp.get_employeeid():
            print("----------------EMPLOYEE INFO-----------------")
            print(f"Employee ID: {emp.get_employeeid()}")
            print(f"First Name: {emp.get_fname()}")
            print(f"Last Name: {emp.get_lname()}")
            print(f"Hire Date: {emp.get_employmentdate()}")
            print(f"Salary: ${emp.get_salary():,.2f}")
            print(f"Department: {emp.get_department()}")
            print("-----------------------------------------------")

            update = int(input("""What information do you want to update? 
                Option 1 - First Name
                Option 2 - Last Name
                Option 3 - Hire Date
                Option 4 - Salary
                Option 5 - Department
            Enter option (Numbers 1-5 Only): """))

            if update == 1:
                new_fname = input("What is the new First Name of the Employee? ")
                emp.set_fname(new_fname)
            if update == 2:
                new_lname = input("What is the new Last Name of the Employee? ")
                emp.set_lname(new_lname)
            if update == 3:
                new_hdate = input("What is the new Hire Date of the Employee? ")
                emp.set_employmentdate(new_hdate)
            if update == 4:
                new_salary = int(input("What is the new Salary of the Employee? "))
                emp.set_salary(new_salary)
            if update == 5:
                new_dept = input("What is the new Department of the Employee? ")
                emp.set_department(new_dept)

            print('\n')
            print("----------------!!!UPDATED EMPLOYEE INFO!!!-----------------")
            print(f"Employee ID: {emp.get_employeeid()}")
            print(f"First Name: {emp.get_fname()}")
            print(f"Last Name: {emp.get_lname()}")
            print(f"Hire Date: {emp.get_employmentdate()}")
            print(f"Salary: ${emp.get_salary():,.2f}")
            print(f"Department: {emp.get_department()}")
            print("-----------------------------------------------------------")
            break
    else:
        print(f"Employee with ID = {emp_id} does not exist!!")
