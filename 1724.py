from typing import List


class Solution:

    def max_cnt(self, arr, start, d):
        t = len(arr) * [False]
        t[start] = True
        cur = start
        left = max(cur - d, 0)
        right = min(cur + d, len(arr) - 1)
        cnt = 1
        flag = False
        while not flag:
            ta = 0
            next = None
            taa = set()
            for i in range(left, right + 1):
                if t[i]:
                    taa.add(1)
                    continue
                if ta < arr[i] < arr[cur]:
                    next = i
                    ta = arr[i]
                    taa.add(0)
            flag = 0 in taa
            if next is None:
                return cnt
            cnt += 1
            left = max(next - d, 0)
            right = min(next + d, len(arr) - 1)
            cur = next

    def maxJumps(self, arr: List[int], d: int) -> int:
        ans = [0] * len(arr)
        for i in range(len(arr)):
            ans[i] = self.max_cnt(arr, i, d)
        print(ans)
        return max(ans)


if __name__ == '__main__':
    S = Solution()
    S.maxJumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12]
               , 2)
