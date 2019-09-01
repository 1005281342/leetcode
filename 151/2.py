from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        ans = []
        for word in words:
            ans.append(word.count(min(word)))

        res = []
        for v in queries:
            vc = v.count(min(v))
            c = 0
            for w in ans:
                if vc > w:
                    c += 1
            res.append(c)

        return res
        # def F(s):
        #     if not s: return 0
        #     ch = min(s)
        #     return s.count(ch)
        #
        # fwords = []
        # for word in words:
        #     fwords.append(F(word))
        #
        # res = []
        # for q in queries:
        #     f_q = F(q)
        #     res.append(sum([f_q < fword for fword in fwords]))
        #
        # return res


if __name__ == '__main__':
    S = Solution()
    S.numSmallerByFrequency(queries=["cbd"], words=["zaaaz"])
    S.numSmallerByFrequency(
        queries=["ba", "a", "baaa", "aaabbbab", "abbbb", "bb", "aaaababbba", "babaaababb", "bbb", "b", "aaaaa",
                 "babbbaab", "bbbaaabab", "bba", "baabbaaab", "bbabbababa", "aaabbab", "aaab"],
        words=["bab", "bab", "bbaaaaab", "aa", "ab", "bb", "bbbaba", "bb", "bba", "aba", "ba", "babbbabaab", "baaabb",
               "abaa", "b", "abbabbb", "b", "abbbba"])
