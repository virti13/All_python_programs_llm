# Parent class
class Employee:

    def employee_info(self):
        print("This is an employee")


# Child class
class Manager(Employee):

    def manager_info(self):
        print("This is a manager")


# Create object
manager = Manager()

# Parent class method
manager.employee_info()

# Child class method
manager.manager_info()