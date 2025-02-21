import numpy as np

class NumPyArray:
    def __init__(self, data):
        """Initialize with a NumPy array."""
        self.data = np.array(data)

    def __repr__(self):
        """Return a string representation of the array."""
        return f"NumPyArray(shape={self.data.shape}, data={self.data})"

    def shape(self):
        """Return the shape of the array."""
        return # TODO: Return the shape of the numpy array

    def mean(self):
        """Compute the mean (without using np.mean)."""
        return # TODO: Compute mean using vectorized operations only. Do not use np.mean() or arr.mean()

    def standard_deviation(self):
        """Compute standard deviation (without using np.std)."""
        return # TODO: Implement without np.std or arr.std()
    
    def is_equal(self, arr):
        """Check if our array is equal another array arr. Return True or False"""
        return # TODO: Implement without using np.equal
    
    def matching_elements_count(self, arr):
        """Count the number of matching elements (element-wise) between this array and another NumPy array."""
        # TODO: Ensure shape matching before element-wise comparison
        if self.data.shape != arr.shape:
            raise ValueError("Arrays must have the same shape for element-wise comparison.")
        return # TODO: Complete this code

    def flatten(self):
        """Flatten the array (without np.flatten)."""
        return # TODO: Implement flatten manually: Hint: Use the reshape() function

    def dot(self, other):
        """Compute dot product without np.dot()."""
        if self.data.shape[-1] != other.data.shape[0]:
            raise ValueError("Shapes do not align for dot product.")
        return # TODO: Implement dot product using matrix multiplication rules

    def unique(self):
        """Find unique elements without np.unique."""
        return # TODO: Return the number of unique elements in our array

    def min_max_normalization(self):
        """Normalize the array between 0 and 1 using Min-Max normalization"""
        return # TODO 

    def elementwise_multiplication(self, other):
        """Perform element-wise multiplication (without using np.multiply)."""
        if self.data.shape != other.data.shape:
            raise ValueError("Shapes must match for element-wise multiplication.")
        return # TODO: Perform element-wise multiplication

    def broadcasting_addition(self, other):
        """Perform broadcasting addition (without using np.add)."""
        return # TODO: Perform broadcasting addition

    def broadcasting_multiplication(self, other):
        """Perform broadcasting multiplication (without using np.multiply)."""
        return # TODO: Perform broadcasting multiplication
