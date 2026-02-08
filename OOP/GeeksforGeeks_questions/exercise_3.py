# Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways.

class Employee:
    '''
    Represents Employee
    
    This class is used to create objects, which used to store and print details of employee
    '''
    def __init__(self, name, id=None, department=None):
        '''
        Initialize an Employee object.

        Args:
            name (str): the name of the employee.
            age (int): the age of the employee.
            salary (float): the salary of the employee.
        '''
        self.name = name
        self.id = id
        self.department = department

    def display_details(self):
        '''
        displays details of employee
        
        Args:
            None
        Returns:
            None
        '''
        print(f"Name: {self.name}")
        if self.id:
            print(f"ID: {self.id}")
        if self.department:
            print(f"Department: {self.department}")
            
employee1 = Employee("John", 85, "HR")
employee1.display_details()