class Solution:
    def fac(self,n):
        ans=1
        for i in range(1,n+1):
            ans*=i
        return ans
    def climbStairs(self, n: int) -> int:
        # t = count(2) , n = count(1)
        ans=1
        t = 0
        while n > 2:
            t+=1
            n-=2
            ans+= self.fac(n+t)/(self.fac(n)*self.fac(t))
        if n == 2:
            ans+=1
        return int(ans)


        