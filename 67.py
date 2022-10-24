class Solution:
    def addBinary(self, a: str, b: str) -> str:
        b_sum = str(bin(int(a,2)+int(b,2)))
        return (b_sum[2:])
