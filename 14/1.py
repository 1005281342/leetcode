class Solution:
    def toHexspeak(self, num: str) -> str:
        x = {"A", "B", "C", "D", "E", "F", "I", "O"}
        xn = hex(int(num))[2:].replace('1', "I").replace('0', 'O')
        if set(xn) | x == x:
            return xn
        return "ERROR"
