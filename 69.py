class Solution:
    def mySqrt(self, x: int) -> int:
        ans=x//2
        while ans*ans > x:
            ans //=2
            if ans == 1:
                ans = 0
        while True:
            if ans*ans > x:
                return ans-1
            else:
                ans+=1