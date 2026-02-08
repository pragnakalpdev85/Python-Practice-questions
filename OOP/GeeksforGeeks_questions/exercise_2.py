# Exercise 2: Develop a class Calculator with methods to add and subtract two numbers.

class Calculator:
    '''
    Represent Calsulator
    
    This class is used to creat objects, which adds and subtract two numbers.
    '''
    
    def add(self, number1: float, number2: float) -> float:
        '''
        Adds two numbers
    
        Args:
            number1 (float): first number
            number2 (float): second number
        Returns:
            float: addition of two numbers
        '''
        return number1 + number2
    
    def subtract(self, number1: float, number2: float) -> float:
        '''
        Subtracts two numbers
    
        Args:
            number1 (float): first number
            number2 (float): second number
        Returns:
            float: subtraction of two numbers
        '''
        return number1 - number2
    
calculator = Calculator()
print(calculator.add(25,27))
print(calculator.subtract(25,10))