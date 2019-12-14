from typing import List
from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.iter = sorted(combinations(characters, combinationLength))
        self.index = 0

    def next(self) -> str:
        t = self.iter[self.index]
        self.index += 1
        return "".join(t)

    def hasNext(self) -> bool:
        return self.index < len(self.iter)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()