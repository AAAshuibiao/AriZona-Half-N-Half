def equation_func(num):
    return -num ** 2 + 2 * num


def get_peak(left_num, right_num, accuracy):
    GR = (5 ** (1/2) - 1) / 2
    d = (right_num - left_num) * GR
    a = left_num + d
    b = right_num - d

    while True:
        fa = equation_func(a)
        fb = equation_func(b)
        if abs(fa - fb) < accuracy and abs(a - b) < accuracy:
            break
        if fa > fb:
            left_num = b
            b = a
            d = (right_num - left_num) * GR
            a = left_num + d
        else:
            right_num = a
            a = b
            d = (right_num - left_num) * GR
            b = right_num - d

    return (fa + fb) / 2


print(
    get_peak(-100, 100, 0.01)
)

input()
