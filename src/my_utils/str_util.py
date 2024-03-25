
def str_reverse(s):
    """
    将传入的字符串反转
    :param s:
    :return:
    """
    return s[::-1]


def sbustr(s, x, y, z):
    """
    截取字符串
    :param s: 传入的字符串
    :param x: 起始下标
    :param y: 截止下标
    :param z: 步长
    :return:
    """
    return s[x:y:z]


if __name__ == '__main__':
    print(str_reverse("helloworld"))
    print(sbustr("helloworld", 0, 5, 2))
