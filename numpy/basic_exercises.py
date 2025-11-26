import sys
import numpy as np


def create_array():
    """create simple arrays"""
    a = np.array([[1,2,3], [4, 5, 6]])
    print("two dimensional array: ", a)

    b = np.array([1, 2, 3, 4])
    print("one dimensional array: ", b)

    c = np.array([[1,2,3], [4, 5, 6], [7,8,9]])
    print("three dimensional array: ", a)


def create_arrays_with_zeros_and_ones():
    """create simple arrays with zeroes and ones"""
    a = np.zeros(5)
    print("one dimensional array with zeros: ", a)

    b = np.ones((2, 3))
    print("2x3 matrix of ones: ", b)


def arrays_shape_and_size():
    """shows the size and shape of an array"""
    a = np.array([1, 2, 3, 4])
    b = np.array([[1, 2, 3], [2, 4, 5], [2, 5, 6]])

    print("array a: ", a)
    print("shape of a: ", a.shape)
    print("size of a: ", a.size)

    print("array b: ", b)
    print("shape of b: ", b.shape)
    print("size of b: ", b.size)


def array_flatting():
    """flattens an array"""
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print("array a: ", a)
    print("flattened array: ", a.flatten())


def array_aggregations():
    """ """
    m = np.array([[1, 2, 3], [4, 5, 6]])
    print("array m: ", m, end="\n\n")
    print("sum of all elements of m: ", m.sum())  # 21
    print("mean of m: ", m.mean())  # 3.5
    print("m's standard deviation: ", m.std())  # 1.707...
    print("m's var: ", m.var())  # 2.916...
    print("m's min: ", m.min(), m.max())  # (1, 6)

    print("sum of m's axis 0: ", m.sum(axis=0))  # [5 7 9] (columns)
    print("sum of m's axis 1: ", m.sum(axis=1))  # [6 15] (rows)


def random_numbers():
    """generate random numbers"""
    print("random numbers in a given shape: ", np.random.rand(3))  # e.g. [0.3, 0.7, 0.1]
    print("random numbers from 'standard normal' distribution: ", np.random.randn(3))  # e.g. [-1.1, 0.4, 0.8]
    print("random integers from low (inclusive) to high (exclusive): ", np.random.randint(0, 10, 5))


def detect_and_replace_missing_values():
    """"""
    a = np.array([1, np.nan, 3])
    np.isnan(a)
    # [False True False]
    np.nanmean(a)
    # 2.0
    np.nan_to_num(a, nan=0)
    # [1. 0. 3.]


def vectorized_operations():
    """several vectorized operations"""

    # Traditional loop approach
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])

    # Vectorized approach
    a_np = np.array([1, 2, 3, 4, 5])
    b_np = np.array([6, 7, 8, 9, 13])
    result_np = a_np + b_np  # [7, 9, 11, 13, 15]
    print("a_np: ", a_np)
    print("b_np: ", b_np)
    print("result of vectorized operation (a_np + b_np): ", result_np)
    print("result of vectorized operation (a_np - b_np): ", a_np - b_np)


def broadcasting():
    a = np.array([1, 2, 3])
    print("array a: ", a)
    print("array a + a scalar value (10): ", a + 10)

    m = np.array([[1, 2, 3], [4, 5, 6]])
    v = np.array([10, 20, 30])
    print("array m: ", m)
    print("vector v: ", v)
    print("m + v: ", m + v)
    m + v




def main():

    print("\n")
    print("1 - Create simple arrays",end="    ")
    print("2 - Create arrays filled with zeros or ones", end="    ")
    print("3 - Show array's shape and size", end="    ")
    print("4 - Flatten array", end="    ")
    print("5 - Array aggregations")
    print("6 - Random numbers",end="          ")
    print("7 - detect_and_replace_missing_values", end="          ")
    print("8 - vectorized_operations", end="          ")
    print("9 - broadcasting")
    print("__________________________________________________________________"
          "__________________________________________________________________________________________")

    try:
        choice = int(input("Choose an algorithm (type zero to exit): "))
    except ValueError:
        print("Please enter a valid number.")
        return


    match choice:

        case 0:
            sys.exit()

        case 1:
            create_array()

        case 2:
            create_arrays_with_zeros_and_ones()

        case 3:
            arrays_shape_and_size()

        case 4:
            array_flatting()

        case 5:
            array_aggregations()

        case 6:
            random_numbers()

        case 7:
            detect_and_replace_missing_values()

        case 8:
            vectorized_operations()

        case 9:
            broadcasting()



main()