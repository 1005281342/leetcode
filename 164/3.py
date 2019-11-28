from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        t = products
        t.sort()
        res = list()
        for i in range(1, len(searchWord)):
            tmp = list()
            for word in t:
                if searchWord[0:i] == word[0:i]:
                    tmp.append(word)
            res.append(tmp[:3])
            t = tmp
        return res


if __name__ == '__main__':
    s = [["mobile", "moneypot", "monitor", "mouse", "mousepad"],
         ["mobile", "moneypot", "monitor", "mouse", "mousepad"],
         ["mouse", "mousepad"],
         ["mouse", "mousepad"]]