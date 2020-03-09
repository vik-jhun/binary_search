def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.
    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.
    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''

    left = 0
    right = len(xs)-1

    def go(left, right):
        mid = (left+right)//2
        if xs[mid] == 0:
            return mid+1
        if left == right:
            if xs[mid]>0:
                return  mid 
            else:
                return None

        if xs[mid]>0:
            return go(left, mid-1)
        if xs[mid]<0:
            return go(mid+1, right)

    if len(xs) == 0:
        return None
    if xs[0]>0:
        return 0
    else:
        return go(left,right)



def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.
    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.
    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''

    left = 0
    right = len(xs)-1

    if len(xs) == 0:
        return 0

    def morethan(left,right):
        mid = (left+right)//2
        if xs[mid] == x:
            if mid == 0 or xs[mid-1] > x:
                return mid
            else:
                return morethan(left, mid-1)
            if left == right:
                return None
            if x < xs[mid]:
                return morethan(mid+1, right)
            if x > xs[mid]:
                return morethan(left, mid-1)

    def lessthan(left, right):
        mid = (left+right)//2
        if x == xs[mid]:
            if mid == len(xs)-1 or x > xs[mid+1]:
                return mid
            else:
                return lessthan(mid+1, right)
        if left == right:
            return None
        if x < xs[mid]:
            return lessthan(mid+1, right)
        if x > xs[mid]:
            return lessthan(left, mid-1)
        
    a = morethan(left, right)
    b = lessthan(left, right)

    if a == None or b  == None:
        return 0
    else:
        return b-a+1


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]
    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]
    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''

    if hi-lo < epsilon:
        return hi

    else: 
        high_value = f(hi)
        low_value = f(lo)

        mid = (hi+lo)/2
        m1 = (mid+lo)/2
        m2 = (mid+hi)/2

        m1_value = f(m1)
        m2_value = f(m2)

        minimized = min(low_value, m1_value, m2_value, high_value)

        if minimized  == low_value or minimized == m1_value:
            return argmin(f, lo, m2, epsilon) 
        else:
            return argmin(f, m1, hi, epsilon)

