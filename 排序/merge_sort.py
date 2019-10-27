def merge(a: list, b: list) -> list:
    if not a or not b:
        return a + b
    la = len(a)
    lb = len(b)
    ia, ib = 0, 0
    c = list()
    while ia < la and ib < lb:
        if a[ia] < b[ib]:
            c.append(a[ia])
            ia += 1
        elif b[ib] < a[ia]:
            c.append(b[ib])
            ib += 1
        else:
            c.append(a[ia])
            c.append(b[ib])
            ia += 1
            ib += 1
    c.extend(a[ia:])
    c.extend(b[ib:])
    return c


def merge_sort(arr: list) -> list:
    length = len(arr)
    if length <= 1:
        return arr
    index = length // 2
    return merge(merge_sort(arr[:index]), merge_sort(arr[index:]))


if __name__ == '__main__':
    arr = [2, 5, 16, 2, 6, 7, 2, 1, 2, 4, 5, 3]
    s = merge_sort(arr)
    print(s)
