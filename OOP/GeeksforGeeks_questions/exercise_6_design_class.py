# Design a class as described below.

# class name : MyClass
# function: function name - display(), parameters - none, return type - void , access modifier - public, function body - 
# should print "Hello World"

class MyClass:
    '''
    This class is used to create objects, which prints hello world
    '''
    def display(self):
        '''
        displays message
        '''
        print("Hello World")

myclass = MyClass()
myclass.display()