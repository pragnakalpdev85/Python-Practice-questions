# Exercise 5: Create a class MaxFinder that identifies the largest number in a list.

class MaxFinder:
    '''
    Reprents class for finding max
    
    This class is used to create objects, which finds max from list
    '''
    
    def __init__(self, numbers: list):
        '''
        Initialize an MaxFinder object
        
        Args:
            numbers (list): list of numbers
        '''
        self.numbers = numbers

    def find_max(self):
        '''
        findes max from a list
        
        Returns:
            max from list
        '''
        if not self.numbers:
            return "List is empty"
        return max(self.numbers)
    
finder = MaxFinder([4,5,8,11,55,555,999])
max  = finder.find_max()
print(max)