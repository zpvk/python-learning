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
            
        """Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute. 
        After reading in the file, the mean and standard deviation are calculated

                        
        Args:
            file_name (string): name of a file to read from

        Returns:
            None
        
                
        """
                    
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
            
        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
    
            
        
    def plot_histogram(self):
                """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.

                
        Args:
            None

                    
        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')

        
        
        
    def pdf(self, x):
                """Probability density function calculator for the gaussian distribution.