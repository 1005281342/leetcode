from typing import List
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], kk: int) -> bool:
        if len(nums) % kk:
            return False

        if len(nums) == 1:
            return True

        cd = Counter(nums)
        ks = sorted(list(cd.keys()))
        # if ks[-1] - ks[0] > len(nums):
        #     return False
        if kk == len(ks):
            if ks[-1] - ks[0] + 1 != kk:
                return False
            for n in ks[1:]:
                if cd[n] != cd[ks[0]]:
                    return False
            return True
        print(ks[:len(ks)-kk+1])
        for k in ks[:len(ks)-kk+1]:
            print(k, cd[k])
            # if cd[k] <= 0:
            #     continue

            while cd[k]:

                cd[k] -= 1
                for d in range(1, kk):
                    if cd[k + d] <= 0:
                        return False
                    cd[k + d] -= 1

        for c in cd.values():
            if c != 0:
                return False
        return True


if __name__ == '__main__':
    S = Solution()
    nums = [12,12,2,11,22,20,11,13,3,21,1,13]
    kk = 3
    res = S.isPossibleDivide(nums, kk)
    print(res)
