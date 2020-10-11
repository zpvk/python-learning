import math
import matplotlib.pyplot as plt

class Gaussian():
        """ Gaussian distribution class for calculating and 
            visualizing a Gaussian distribution.

        Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
                    
    """
    def __init__(self, mu = 0, sigma = 1):
                
        self.mean = mu
        self.stdev = sigma
        self.data = []
        
    
    def calculate_mean(self):
    
        """Function to calculate the mean of the data set.
                
        Args: 
            None
                
        Returns:
            float: mean of the data set
        
            
        """
        avg = 1.0 * sum(self.data) / len(self.data)
                
        self.mean = avg
        
        return self.mean


        
    def calculate_stdev(self, sample=True):

        """Function to calculate  the standard deviation of the data set.
                
        Args:
            sample (bool): whether the data represents a sample or population
                    
        Returns: 
             float: standard deviation of the data set
        
        """
        
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
    
        mean = self.mean
            
        sigma = 0
            
        for d in self.data:
                        sigma += (d - mean) ** 2
                
        sigma = math.sqrt(sigma / n)
    
        self.stdev = sigma
                
        return self.stdev
                

    def read_data_file(self, file_name, sample=True):