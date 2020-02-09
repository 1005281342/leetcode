class Solution:
    def freqAlphabets(self, s: str) -> str:
        a = ord('a')
        d = dict()
        for i in range(0, 9):
            d[str(i + 1)] = chr(a + i)

        for i in range(9, 26):
            # d[str(i + 1) + '#'] = chr(a + i)
            d[str(i + 1)] = chr(a + i)

        aa = list()
        afh = s.split('#')

        if s[-1] == '#':
            for af in afh:
                # af = afh[0]
                if len(af) > 2:
                    for i in af[:len(af) - 2]:
                        aa.append(d[i])
                aa.append(d[af[len(af) - 2:]])

        # for c in afh[1:len(afh) - 1]:
        #     aa.append(d[c])
        else:

            for af in afh[:len(afh) - 1]:
                # af = afh[0]
                if len(af) > 2:
                    for i in af[:len(af) - 2]:
                        aa.append(d[i])
                aa.append(d[af[len(af) - 2:]])

            for c in afh[-1]:
                aa.append(d[c])

        return ''.join(aa)


if __name__ == '__main__':
    S = Solution()
    S.freqAlphabets('a')
