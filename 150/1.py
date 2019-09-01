from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            chars_p = list(chars)
            flag = True
            for a in word:
                if a in chars_p:
                    chars_p.remove(a)
                else:
                    flag = False
                    break
            if flag:
                res += len(word)
        return res


        # cs = set(chars)
        # res = 0
        # for word in words:
        #     if set(word) | cs == cs:
        #         res += len(word)
        #
        # return res