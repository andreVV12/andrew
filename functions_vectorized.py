import numpy as np


def prod_non_zero_diag(x):
    d = np.diag(x)
    return d[d != 0].prod()
    pass


def are_multisets_equal(x, y):
    x_n, x_c = np.unique(x, return_counts=True)
    y_n, y_c = np.unique(y, return_counts=True)
    if(np.shape(x_n) != np.shape(y_n)):
        return False
    if(np.any(x_n != y_n) or np.any(x_c != y_c)):
        return False
    return True
    pass


def max_after_zero(x):
    num = np.where(x[:len(x) - 1] == 0)
    num = np.array(num) + 1
    return np.max(x[(num.tolist())])
    pass


def convert_image(img, coefs):
    return np.sum(img * coefs, axis = -1)
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
    return np.sqrt(np.sum((x[:, np.newaxis] - x) ** 2, axis = -1))
    pass
