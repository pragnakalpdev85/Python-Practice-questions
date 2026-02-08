# Implement the following classes to understand inheritance in Python:

# Class Name: Employee
# Attributes:
# id (int)
# salary (int)
# Constructor: __init__(self, id, salary) — Initializes the values to respective variables.
# Class Name: SalesEmployee (Subclass of Employee)
# Attributes:
# Inherited from Employee: id, salary
# New attribute: sales (int)
# Constructor: __init__(self, id, salary, sales) — Calls super().__init__(id, salary) to initialize id and salary, 
# and initializes the sales attribute.
# Examples:

# Input: id = 14, salary = 30000, sales = 20
# Output: 
# 14 30000
# 14 30000 20

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
        
    def display(self):
        '''displays sales employee details'''
        print(self.id,self.salary,self.sale)

salesemployee = SalesEmployee(85,50000,300000)
salesemployee.display()