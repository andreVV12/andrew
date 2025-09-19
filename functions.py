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
    height = len(img)
    width = len(img[0])
    res_img = list()
    for i in range(height): 
        now_str = list()
        for j in range(width):
            sum = 0
            for k in range(len(coefs)):
                sum += img[i][j][k] * coefs[k]
            now_str.append(sum)
        res_img.append(now_str)
    return res_img
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
    rasst = list()
    for i in range(len(x)):
        ans = list()
        for j in range(len(y)):
            b = 0
            for k in range(len(x[0])):
                b += (x[i][k] - y[j][k]) ** 2
            ans.append(math.sqrt(b))
        rasst.append(ans)
    return rasst
    pass
