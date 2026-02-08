# Design a class as described below:

# Class Name: Addition
# Method:
# Function Name: add
# Parameters: a (int), b (int)
# Return Type: int
# Static: Yes (Use the @staticmethod decorator)
# Task: Returns the sum of the values given as parameters

class Addition:
    '''
    represents Addition class
    
    this class is used to implement static methods
    '''
    @staticmethod
    def add(number1: int, number2: int) -> int:
        '''
        Addes two numbers
        
        Args:
            number1 (int): first number
            number2 (int): second number
        Return:
            int: addition of two numbers
        '''
        return number1+number2
    
print(Addition.add(25,25))