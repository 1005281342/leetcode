import bisect

nums = [1, 21, 2, 6, 87, 100]
res = bisect.bisect(nums, 2)
print(res, nums)

res = bisect.bisect_left(nums, 2)
print(res, nums)
bisect.insort_left(nums, 10000)
bisect.insort_left(nums, 10)
bisect.insort_left(nums, 10)
print(res, nums)

res = bisect.bisect_right(nums, 2)
bisect.insort_right(nums, 1001)
print(res, nums)


def binary_search(nums, x):
    left = 0
    right = len(nums)
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            left = mid
        else:
            right = mid
    return -1


if __name__ == '__main__':

    print(binary_search(nums, 10))


