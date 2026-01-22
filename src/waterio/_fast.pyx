def checksum(int[:] arr) -> int:
    """
    Compute the checksum (sum of elements) of a 1D integer array.

    Parameters
    ----------
    arr : int[:]
        One-dimensional contiguous array of integers.

    Returns
    -------
    int
        Sum of all elements in the input array.
    """
    cdef Py_ssize_t i
    cdef int s = 0

    for i in range(arr.shape[0]):
        s += arr[i]

    return s

