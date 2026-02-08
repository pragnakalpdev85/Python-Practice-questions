# Implement a Python class ComplexNumber to demonstrate operator overloading for adding two complex numbers.

# Class Name: ComplexNumber

# Attributes:

# real (float): The real part of the complex number.
# imaginary (float): The imaginary part of the complex number.
# Constructor:

# __init__(self, real, imaginary): Initializes the real and imaginary attributes with the given values.
# Methods/Functions:

# __add__(self, other):

# Parameters: other (another ComplexNumber object)
# Task: Overload the + operator to add two complex numbers. The addition of two complex numbers (a + bi) and (c + di) 
# is calculated as:
# Real part: a + c
# Imaginary part: b + d
# Return: A new ComplexNumber object representing the sum of the two complex numbers.
# __str__(self):

# Parameters: None
# Task: Overload the string representation of the object to return the complex number in the format "a + bi",
# where a is the real part and b is the imaginary part.
# Examples:

# Input: real1 = 3, imaginary1 = 1, real2 = 1, imaginary2 = 7
# Output: 4 + 8i

class ComplexNumber:
    '''
    represent ComplexNumber with attributes real and imaginary part of number
    '''
    def __init__(self, real: float, imaginary: float):
        '''
        Initialize ComplexNumber object
        
        Args:
            real (float): real part of complex number
            imaginary (float): imaginary part of complex number
        '''
        self.real = real
        self.imaginary = imaginary
        
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
        
    def __add__(self, other):
        '''
        Calculate sum of two complex numbers
        
        Args:
            other (ComplexNumber): other object of complex number
        Returns:
            ComplexNumber: Sum of two complex numbers 
        '''
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
number1 = ComplexNumber(3,1)
number2 = ComplexNumber(1,7)

print(number1 + number2)
        
