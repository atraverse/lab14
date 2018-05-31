import ctypes
import sys
# Implements the Array ADT using array capabilities of the ctypes module.

class Array :
    # Creates an array with size elements.
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    # Returns the size of the array.
    def __len__( self ):
        return self._size

    # Gets the contents of the index element.
    def __getitem__( self, index ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    # Puts the value in the array element at index position.
    def __setitem__( self, index, value ):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value

    # Clears the array by setting each element to the given value.
    def clear( self, value ):
        for i in range( len(self) ) :
            self._elements[i] = value


if __name__=="__main__":
    value_list = Array(9)
    # print('size of array = ', sys.getsizeof(value_list))

    value_list[0]='X'
    value_list[1]='O'
    for i in range(len(value_list)):
        print(value_list[i])
    # for i in range(3):
    #     for j in range(3):
    #         print(value_list[i], end='')
    #     print('')