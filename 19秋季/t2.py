def fun1(a,b):
    x = a % b
    while (x != 0):
        a = b
        b = x
        x = a % b
    return b

if __name__ == '__main__':

    res = fun1(301, 3)
    print(res)