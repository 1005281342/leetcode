from collections import defaultdict


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.dd = defaultdict(set)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        for i in range(10):

            if message in self.dd[timestamp-i]:
                return False

        self.dd[timestamp].add(message)
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)