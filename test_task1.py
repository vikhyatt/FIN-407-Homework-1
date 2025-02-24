import numpy as np
from task1 import NumPyArray


a = np.array([[1, 2, 6], [4, 5, 6]])  
c = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])  
min_max = np.array([[0., 0.2, 1. ], [0.6, 0.8, 1. ]])
elem_multi = np.array([[ 1,  4, 18], [16, 25, 36]])
broad_add = np.array([[11, 22, 36], [14, 25, 36]])
broad_multi = np.array([[10,  40, 180], [ 40, 100, 180]])
other = np.ones([10,12,3,5])
data = NumPyArray(a)
failed = 0

try:
    assert data.shape() == a.shape
except:
    failed += 1
    print(".shape() test failed")

try:
    assert data.mean() == a.mean()
except:
    failed += 1
    print('.mean() test failed')

try:
    assert data.standard_deviation() == a.std()
except:
    failed += 1
    print('.std() test failed')

try:
    assert not data.is_equal(c)
except:
    failed += 1
    print('.is_equal() test failed')

try:
    assert data.matching_elements_count(c) == 5
except:
    failed += 1
    print('.matching_elements_count() test failed')

try:
    assert (data.flatten() == a.flatten()).all()
except:
    failed += 1
    print('.flatten() test failed')

try:
    assert set(data.unique()) == set(np.unique(a))
except:
    failed += 1
    print('.unique() test failed')

try:
    assert (data.dot(other) == np.dot(a, other)).all()
except:
    failed += 1
    print('.dot() test failed')

try:
    assert (data.min_max_normalization() == min_max).all()
except:
    failed += 1
    print('.min_max_normalization() test failed')

try:
    assert (data.elementwise_multiplication(c) == elem_multi).all()
except:
    failed += 1
    print('.elementwise_multiplication() test failed')

try:
    assert (data.broadcasting_addition(b) == broad_add).all()
except:
    failed += 1
    print('.broadcasting_addition() test failed')

try:
    assert (data.broadcasting_multiplication(b) == broad_multi).all()
except:
    failed += 1
    print('.broadcasting_multiplication() test failed')

if failed == 0:
    print('All methods evaluated succesfully')