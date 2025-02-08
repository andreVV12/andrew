import numpy as np


def prod_non_zero_diag2(x):
    d = np.diag(X)
    return d[d != 0].prod()
    pass


def are_multisets_equal2(x, y):
    x_n, x_c = np.unique(x, return_counts=True)
    y_n, y_c = np.unique(y, return_counts=True)
    if(np.shape(x_n) != np.shape(y_n)):
        return False
    if(np.any(x_n != y_n) or np.any(x_c != y_c)):
        return False
    return True
    pass


def max_after_zero2(x):
    a = np.ones((1))
    a = np.hstack((curr, x))
    b = a == 0
    return np.max(b[ind[:-1]])
    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """

    pass


def run_length_encoding(x):
    y = np.hstack((np.ones(1), x[:- 1]))
    p = x != y
    p[0] = True
    i1 = np.arange(np.size(x))[p]
    i2 = np.hstack((i1[1:], np.array([np.size(x)])))
    return x[p], i2 - i1
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vctorized implementation.
    """

    pass
