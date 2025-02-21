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
        return # TODO: Return the shape

    def mean(self):
        """Compute the mean (without using np.mean)."""
        return # TODO: Compute mean using vectorized operations only

    def standard_deviation(self):
        """Compute standard deviation (without using np.std)."""
        return # TODO: Implement without np.std

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
        # TODO: Create a mask to find unique elements efficiently
        sorted_arr = np.sort(self.data.flatten())
        mask = np.concatenate(([True], sorted_arr[1:] != sorted_arr[:-1]))
        return sorted_arr[mask]


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

# Sample Test Cases
arr = NumPyArray([[1, 2, 3], [4, 5, 6]])
print(arr.shape())          # Expected: (2, 3)
print(arr.mean())           # Expected: (sum of all elements) / total elements
print(arr.standard_deviation())  # Expected: Std computation
arr.insert(1, 99)           # Insert 99 at index 1
print(arr)
print(arr.flatten())        # Convert to 1D array
print(arr.unique())         # Return unique values
print(arr.moving_average(2))  # Compute moving average with window size 2
print(arr.min_max_normalization())  # Normalize array

# Additional test cases
arr1 = NumPyArray([1, 2, 3])
arr2 = NumPyArray([4, 5, 6])
print(arr1.elementwise_multiplication(arr2))  # Element-wise multiplication
print(arr1.broadcasting_addition(arr2))       # Broadcasting addition
print(arr1.broadcasting_multiplication(arr2)) # Broadcasting multiplication