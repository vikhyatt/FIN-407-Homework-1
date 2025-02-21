"""
The Goal of this Task is to recreate the functionality of Python Lists. For this, we define a custom Class, called CustomList,
and implement our implementations of basic list functionalities in this class. You might notice that some of the methods in the
class are starting and ending with underscores. These methods are referred to as dunder (magic) methods. These are special 
methods that provide built-in behavior for objects, allowing customization of how instances of the class interact with 
Python’s built-in operations.
"""

class CustomList:
    def __init__(self, values):
        """Initialize the list with a sequence of given values. The values are of class List"""
        self.data =  # TODO: Store values in a Python List

    def __repr__(self):
        """Return a string representation of the list."""
        return f"CustomList(items={self.data})"

    def __len__(self):
        """Return the number of elements in the list."""
        return  # TODO: Implement length calculation without using the inbuilt "len" function

    def append(self, value):
        """Add a value to the end of the list."""
        # TODO: Implement append without using Python lists

    def pop(self):
        """Remove and return the last element of the list"""
        if __________:  # TODO: Handle edge case (empty list), Hint: You can call some other method defined in this Class
            raise IndexError("Pop from empty CustomList")
        
        return # TODO: Implement pop without using the pop function of lists

    def __getitem__(self, index):
        """Retrieve element at a given index."""
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        return  # TODO: Implement index-based retrieval. Do not use the indexing of Python lists

    def __setitem__(self, index, value):
        """Set element at a given index."""
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        
        # TODO: Implement index-based assignment. Do not return anything

    def insert(self, index, value):
        """Insert value at a specific index."""
        if index < 0:
            index = 0
        elif index > len(self):
            index = len(self)

        # TODO: Implement insert (without using `list.insert`). Hint: Use slicing of Python lists

    def remove(self, value):
        """Remove the first occurrence of value."""
        for i in range(len(self)):
            if self[i] == value:
                __________  # TODO: Remove value from self.data
                return None
        raise ValueError(f"{value} not in list")

    def sort(self):
        """Sort the list in ascending order using selection sort (without `sorted()`)."""
        n = len(self)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self[j] < self[min_idx]:
                    min_idx = j
            __________  # TODO: Swap elements at i and min_idx

    def reverse(self):
        """Reverse the order of elements."""
        left, right = 0, len(self) - 1
        while left < right:
            __________  # TODO: Swap left and right elements
            left += 1
            right -= 1

    def __iter__(self):
        """Make the class iterable."""
        self._index = 0
        return self

    def __next__(self):
        """Return the next element in iteration."""
        if self._index >= len(self):
            raise StopIteration
        value =  # TODO: Get current value
        self._index += 1
        return value

    def map(self, func):
        """Apply a function func to each element in the list."""
        return  # TODO: Fill this using list comprehension

    def __add__(self, other):
        """Concatenate two CustomLists (overloading `+` operator)."""
        if not isinstance(other, CustomList):
            raise TypeError("Can only concatenate CustomList with CustomList")
        return  # TODO: Implement concatenation
