# Implement the following classes to understand method overriding in Python:

# Class Name: Employee

# Attributes:

# id (integer)
# salary (integer)
# Constructor:

# __init__(self, id, salary): Initializes the id and salary attributes with the given values.
# Methods/Functions:

# get_info(self):
# Parameters: None
# Task: Returns a string formatted as: "EmployeeID:{id} Salary:{salary}".
# Class Name: SalesEmployee (Subclass of Employee)

# Attributes:

# Inherited from Employee: id, salary
# New attribute: sales (integer, optional, defaults to 0)
# Constructor:

# __init__(self, id, salary, sales=0): Calls super().__init__(id, salary) to initialize the inherited attributes, and initializes the sales attribute. The sales parameter defaults to 0 if not provided.
# Methods/Functions:

# get_info(self):
# Parameters: None
# Task: Overrides the get_info method to include the sales attribute in the output.
# Return Format: "EmployeeID:{id} Salary:{salary} Sales:{sales}".

class Employee:
    '''
    Represents Employee with attributes id and salary
    '''
    def __init__(self, id: int, salary: int):
        '''
        Initialize employee object
        
        Args:
            id (int): id of the employee
            salary (int): salary of the employee
        '''
        self.id = id
        self.salary = salary  
    
    def get_info(self) -> str:
        '''
        gets information of employee
        
        Retruns:
            str: employee information
        '''
        return f"EmployeeID: {self.id} Salary: {self.salary}"
        
class SalesEmployee(Employee):
    '''
    Represent sales employee with attributes id, salary and sales
    '''
    def __init__(self, id, salary, sale):
        '''
        Initialize sales employee object
        
        Args:
            id (int): id of the sales employee
            salary (int): salary of the sales employee
            sale (int): sale total of the sales employee
        '''
        super().__init__(id, salary)
        self.sale = sale
        
    def get_info(self):
        '''
        gets information of sales employee
        
        Retruns:
            str: sales employee information
        '''
        return f"EmployeeID: {self.id} Salary: {self.salary} Sales: {self.sale}"
    
employee = Employee(25,80000)
print(employee.get_info())

salesemployee = SalesEmployee(85,50000,300000)
print(salesemployee.get_info())