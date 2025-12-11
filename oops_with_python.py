"""
In this file i wanted learn about all oops concept
Now starting from the Class 
--CLASS--
Class is user defined data type, it consist of data member and member function, which can be accessed and used by creating 
an instance of class, its represent the set of properties or method which are common for all object of one type,
Its like blueprint of object 
--
CLASS also considered one fo pillars of OOPS
lets create one class 
"""    

import numpy as np 
import sys

class ArrayState:
    def __init__ (self,data):
        self.data = np.array(data)

    def mean(self):
        return np.mean(self.data)   

    def max_val(self):
        return np.max(self.data)
    def reshape(self,row,  col):
        self.data = self.data.reshape(row ,col)
        return self.data
    def sum_elements(self):
        return np.sum(self.data)  

def main():
    data  = [int(x) for x in sys.argv[1:] ] 
    arr = ArrayState(data)
    print(arr.mean())
    print(arr.max_val())
    print(arr.reshape(3,2))
    print(arr.sum_elements())   


if __name__ == "__main__":
    main()
