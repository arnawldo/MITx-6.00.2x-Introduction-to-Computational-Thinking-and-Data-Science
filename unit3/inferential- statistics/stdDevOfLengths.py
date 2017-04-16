def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import numpy as np

    lengths = np.array( [len(my_string) for my_string in L] ) # string lengths
    x_minus_mu_squared = (lengths - lengths.mean()) ** 2

    var =  x_minus_mu_squared.sum() / len(L)

    return np.sqrt(var)