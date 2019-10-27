from random import randint


def quick_sort(arr: list) -> list:
    length = len(arr)
    if length <= 1:
        return arr

    tmp = arr[randint(0, length-1)]
    low, mid, high = list(), list(), list()
    for num in arr:
        if num < tmp:
            low.append(num)
        elif num > tmp:
            high.append(num)
        else:
            mid.append(num)
    low, high = quick_sort(low), quick_sort(high)
    return low + mid + high


if __name__ == '__main__':
    arr = [2, 5, 16, 2, 6, 7, 2, 1, 2, 4, 5, 3]
    s = quick_sort(arr)
    print(s)
