from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # cnt = 0
        # for i in range(len(arr) - k+1):
        #     if sum(arr[i:i + k]) / k >= threshold:
        #         cnt += 1
        # return cnt

        cnt = 0
        a = sum(arr[:k])
        if a / k >= threshold:
            cnt += 1
        for i in range(len(arr) - k):
            a = a - arr[i] + arr[i + k]
            if a / k >= threshold:
                cnt += 1
        return cnt


if __name__ == '__main__':
    S = Solution()
    S.numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5)
    S.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4)
