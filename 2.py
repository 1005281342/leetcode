from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
    List[int]:

        if veganFriendly:
            tmp = list()
            for i, v in enumerate(restaurants):
                if v[2] != veganFriendly or v[3] > maxPrice or v[4] > maxDistance:
                    continue
                tmp.append((v[1], v[0]))
            ans = list()
            for _, i in sorted(tmp, reverse=True):
                ans.append(i)
            return ans

        tmp = list()
        for i, v in enumerate(restaurants):
            if v[3] > maxPrice or v[4] > maxDistance:
                continue
            tmp.append((v[1], v[0]))
        ans = list()
        for _, i in sorted(tmp, reverse=True):
            ans.append(i)
        return ans
