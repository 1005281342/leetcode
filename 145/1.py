class Solution:
    def relativeSortArray(self, arr1: list, arr2: list) -> list:

        res = []

        for a2 in arr2:
            while True:
                try:
                    arr1.remove(a2)
                    res.append(a2)
                except:
                    break
        return res + sorted(arr1)


S = Solution()
res = S.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])
print(res)
