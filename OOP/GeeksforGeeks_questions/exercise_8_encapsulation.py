# Your task is to create a Person class in Python that demonstrates encapsulation. This class should have two "private" 
# attributes:

# name (String) with a default value of "Geeks".
# age (int) with a default value of 10.
# The class should provide public methods to access and modify these private attributes:

# Getter Methods: get_name() and get_age()
# Setter Methods: set_name(name) and set_age(age)

# Example:

# Input: Funtion calls: [Person(), get_name(), set_name("John"), set_age(21), get_name(), get_age()] 
# Output: John 21
# Explanation: 
# person = Person() // Person Object Created
# person.set_name("John") // name value set to "John"
# person.set_age(21) // age value set to 21
# person.get_name() // "John" returned
# person.get_age() // 21 returned

class Person:
    '''
    Represent Person, whose attributes are name,and age
    
    This class is used to create objects, which gets and sets the attributes of person
    '''
    
    def __init__(self, name: str, age: int):
        '''
        initialize person's attributes
        
        Args:
            name (str): name of the person
            age (int): age of the person
        '''
        self.__name = name
        self.__age = age
        
    def get_name(self) -> str:
        '''
        Gets the name of the person
        
        Returns:
            str: name of the person
        '''
        return self.__name
    
    def get_age(self) -> int:
        '''
        Gets the age of the person
        
        Returns:
            int: age of the person
        '''
        return self.__age
    
    def set_name(self, name: str):
        '''
        sets the name of the person
        
        Args:
            name (str): name of the person
        '''
        self.__name = name
        
    def set_age(self, age: int):
        '''
        sets the age of the person
        
        Args:
            age (int): age of the person
        '''
        self.__age = age
        
person = Person("Name",0)
person.set_name("John") 
person.set_age(21) 
print(person.get_name())
print(person.get_age())
