class Solution:
    def intToRoman(self, num: int) -> str:
        sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans = ""
        run = 0

        while num>0:
            if num >= val[run]:
                ans+=sym[run]
                num-=val[run]
                # print(ans)
            else:
                run+=1
        return ans