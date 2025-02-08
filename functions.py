def prod_non_zero_diag(x):
    l = min(len(x), len(x[0]))
    p = 1
    for i in range(l):
        if(x[i][i]):
            p *= x[i][i]
    return p
    pass


def are_multisets_equal(x, y):
    if(len(x) != len(y)):
        return False
    x.sort()
    y.sort()
    for i in range(len(x)):
        if(x[i] != y[i]):
            return False
    return True
    pass


def max_after_zero(x):
    mx = max(x)
    for i in range(1, len(x)):
        if (not(x[i - 1])) :
            mx = max(mx, x[i])
    return mx
    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    ans = [x[0]]
    ansl = list()
    k = 1
    for i in range(1, len(x)):
        if(x[i - 1] == x[i]):
            k += 1
        else:
            ans.append(x[i])
            ansl.append(k)
            k = 1
    ansl.append(k)
    return (ans, ansl)
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass
