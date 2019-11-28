from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict()
        di = dict()
        for i, v in enumerate(nums2):
            d[v] = i
            di[i] = v
        print(d)
        print(di)
        res = list()
        for num in nums1:
            x = True
            for i in range(d[num], len(nums2)):
                # print(di[i])
                if di[i] > num:
                    res.append(di[i])
                    x = False
                    break
            if x:
                res.append(-1)

        return res


if __name__ == '__main__':
    S = Solution()
    res = S.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
    print(res)