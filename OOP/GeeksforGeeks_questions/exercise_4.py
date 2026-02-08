# Exercise 4: Design a class SeriesCalculator that calculates the sum of an arithmetic series.

class SeriesCalculator:
    '''
    Represents SeriesCalculator
    
    This class is used to create objects, which calculates sum of arithmetic series
    '''
    def calculate_sum(self, number: int, a=1, d=2):
        '''
        calculates sum of arithmetic series
        
        Args: 
            number (int): number till sum to be calculated
            a,d (int): constants
        Returns:
            Int: sum of the arithmetic series
        
        :param self: Description
        :param n: Description
        :param a: Description
        :param d: Description
        '''
        return number * (number + 1)// 2
    
calculate = SeriesCalculator()
print(calculate.calculate_sum(5))