# Implement the following classes to understand abstraction in Python :

# Class Name: Shape (Abstract Class)
# Attributes: color (String)
# Constructor: Shape(c) -> assign value of c to color attribute
# Methods: get_color() -> returns value of color
#          get_area() -> abstract method with float return type
# Class Name: Square (extends Shape)
# Attributes: side (float)
# Constructor: Square(c, side) -> calls super(c) to initialize the color and assigns the value to side.
# Methods: get_area() -> returns the area of the square (side * side).
# Example:

# Input: color = "red", side = 5.0
# Output: 
# red 25.0
from abc import abstractmethod
class Shape:
    '''
    Represents shape, It's attribute is color
    
    This class used to implement methods which are abstract
    '''
    def __init__(self, color: str):
        '''
        Initialize shape object
        
        Args:
            color (str): color of the shape
        '''
        self.color = color
        
    def get_color(self) -> str:
        '''
        gets color
        
        Returns:
            str: color of the shape
        '''
        return self.color
    
    @abstractmethod
    def get_area(self) -> float:
        '''
        calculates area of the shape
        
        Returns:
            float: area of the shape
        '''
        return
    
class Square(Shape):
    '''
    Represent square shape
    
    This class is used to create object which get color of shape and calculates area
    '''
    
    def __init__(self, color:str, side: float):
        '''
        initialize square objects
        
        Args:
            color (str): color of the square
            side (float): sides of the square
        '''
        super().__init__(color)
        self.side = side
        
    def get_color(self):
        '''
        gets color
        
        Returns:
            str: color of the square
        '''
        return super().get_color()
    
    def get_area(self):
        '''
        calculates area of the square
        
        Returns:
            float: area of the square
        '''
        return self.side**2
    
square = Square("Red",4.5)
print(square.get_color())
print(square.get_area())
