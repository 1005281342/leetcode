from typing import List


class Solution:

    def transformArray(self, arr: List[int]) -> List[int]:

        length = len(arr)
        if length <= 2:
            return arr

        flag = True
        while flag:
            p = 1
            flag = False
            while p < length - 1:
                if arr[p - 1] > arr[p] and arr[p] < arr[p + 1]:
                    arr[p] += 1
                    flag = True
                if arr[p - 1] < arr[p] and arr[p] > arr[p + 1]:
                    arr[p] -= 1
                    flag = True
                p += 1
        return arr


if __name__ == '__main__':
    S = Solution()
    # [1,6,3,4,3,5]
    res = S.transformArray([2, 1, 2, 1, 1, 2, 2, 1])
    S.transformArray()
    print(res)