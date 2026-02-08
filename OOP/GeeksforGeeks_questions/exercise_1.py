# Exercise 1: Create a class Greeter with a method greet(name) that prints a greeting for the provided name.

class Greeter:
    '''
    Represent a Greeter
    
    This class used to creat objects, which is used to print greet message
    '''
    
    def greet(self, name: str):
        '''
        prints greet message.
        
        Args:
            name (str): name of the person
        Retruns:
            None
        '''
        print(f"Hello, {name}")
 
#object of Greeter class        
greets = Greeter()
greets.greet("John")