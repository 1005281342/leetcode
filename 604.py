def init(compressedString: str):
    nsd = list()
    cnt = 0
    a = ""
    b = ""
    for i in compressedString:
        if i in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            b += i
        else:
            a += i
            if b:
                ib = int(b)
                nsd.append(ib)
                cnt += int(b)
                b = ""
    nsd.append((a[-2], int(b)))
    cnt += int(b)
    return nsd, cnt, a


class StringIterator:

    def __init__(self, compressedString: str):
        self.cur = 0
        self.d, self.length, self.a = init(compressedString)
        self.nc = 0

    def next(self) -> str:

        if self.hasNext():
            self.cur += 1
            if self.d[self.nc]:
                self.d[self.nc] -= 1
                return self.a[self.nc]
            else:
                self.nc += 1
                if self.hasNext():
                    self.d[self.nc] -= 1
                    return self.a[self.nc]
                else:
                    return " "
        else:
            return " "

    def hasNext(self) -> bool:
        return self.cur < self.length and self.nc < len(self.a)

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
