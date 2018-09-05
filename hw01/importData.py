import numpy as np


# Import data as from txt file and convert to numpy ndarray
def getData(filename):
    data = np.genfromtxt(filename, delimiter='')
    return data
