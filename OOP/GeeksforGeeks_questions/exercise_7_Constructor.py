# Design a class as described below.

# class: User
# instance variable: name(String)
# constructor: parameter: none, task: initialize the instance variable to "Default"

class User:
    '''
    Represents User
    
    This class is used to create objects, which displays users
    '''
    def __init__(self, name: str):
        '''
        initialize users
        
        Args:
            name (str): name of the users
        '''
        self.name = name
        
    def display_user(self):
        '''
        displays user
        '''
        print(self.name)
        
user = User("John")
user.display_user()