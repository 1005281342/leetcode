from typing import List
from collections import defaultdict

d = {
    "minute": 60,
    "hour": 3600,
    "day": 3600 * 24
}


class TweetCounts:

    def __init__(self):
        # self.dd = defaultdict(set)
        self.nad = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        # self.dd[time].add(tweetName)
        self.nad[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:

        dd = d[freq]
        cnt = startTime // dd
        ans = cnt * [0]
        # while endTime >= cnt * dd:
        #     c = 0
        #     for t in range(cnt * dd, (cnt + 1) * dd):
        #         if self.dd.get(t) and tweetName in self.dd[t]:
        #             c += 1
        #     ans.append(c)
        #     cnt += 1
        # return ans
        ns = self.nad[tweetName]
        ns.sort()
        while endTime >= cnt * dd:
            c = 0
            for tx in ns:
                if cnt * dd <= tx < (cnt + 1) * dd:
                    c += 1
                if tx >= (cnt + 1) * dd:
                    break
            ans.append(c)
            cnt += 1
        return ans

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
