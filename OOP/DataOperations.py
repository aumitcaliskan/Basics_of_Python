import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataOperations():

    """
    Convert data to pandas dataframe. If given data is already a dataframe, just read it.
    Give statistical information about the numerical columns.
    Visualize the dataframe as boxplot and scatterplot.
    """

    def __init__(self,data=np.random.rand(100,2),dataframe=pd.DataFrame()):
        self.data = data
        self.dataframe = dataframe

    def read_file(self):

        """
        Read numpy array, json string and csv file; convert to a dataframe.
        Default data: np.random.rand(100,2).
        """

        if isinstance(self.data,np.ndarray):
            self.dataframe = pd.DataFrame(self.data)

        elif isinstance(self.data,pd.core.frame.DataFrame):
            self.dataframe = self.data

        else:
            if '.csv' in self.data:
                self.dataframe = pd.read_csv(self.data)

            elif '.json'in self.data:
                self.dataframe = pd.read_json(self.data)

            else:
                self.dataframe = self.data

        return self.dataframe

    def describe(self):

        """
        Calculate statistical data of count, mean, std, min, max, %25, %50 and %75 quartile values.
        """

        return self.dataframe.describe()

    def bar_plot(self, var1, var2, hue=None, color=None):

        """
        Show point estimates and confidence intervals as rectangular bars.
        Parameters:
        -----------
        var1, var2 : Names of variables in dataframe.
        hue        : Optional.
        color      : Color for all of the elements, optional.
        """

        sns.barplot(x=var1, y=var2, data=self.dataframe, hue=hue, color=color)
        plt.show()

    def scatter_plot(self,var1,var2,hue=None, marker='o'):

        """
        Draw a scatter plot.
        Parameters:
        -----------
        var1, var2 : Names of variables that specify positions on the x and y axes.
        hue        : Optional.
        marker     : Determining how to draw the marker.
        """

        sns.scatterplot(x=var1, y=var2, data=self.dataframe, hue=hue, marker=marker)
        plt.show()

# CSV FILE

csv_dataset = DataOperations(data = 'cement_slump.csv')
csv_dataset.read_file()

csv_dataset.describe()

plt.figure(figsize = (12,6))
csv_dataset.bar_plot(var1 = 'SP', var2 = 'Compressive Strength (28-day)(Mpa)')

plt.figure(figsize = (12,6))
csv_dataset.scatter_plot(var1 = 'Cement', var2 = 'Water', marker = '+')

# JSON FILE

json_dataset = DataOperations('iris.json')
json_dataset.read_file()

json_dataset.describe()

plt.figure(figsize = (12,6))
json_dataset.bar_plot(var1 = 'sepalLength', var2 = 'petalWidth')

plt.figure(figsize = (12,6))
json_dataset.scatter_plot(var1 = 'sepalWidth', var2 = 'petalLength', hue = 'species')

# NUMPY ARRAY

numpy_dataset = DataOperations(np.array([0,1,2,4,5,6]))
numpy_dataset.read_file()

numpy_dataset.describe()

# DATAFRAME

pandas_dataframe = np.array([0,1,2,4,5,6])

pandas_dataset = DataOperations(pandas_dataframe)
pandas_dataset.read_file()

pandas_dataset.describe()

# DEFAULT DATASET

default_dataset = DataOperations()
default_dataset.read_file()

default_dataset.describe()
