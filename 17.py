class Solution:
    def letterCombinations(self, digits: str):
        d = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz",
        }

        temp = [d[int(e)] for e in digits]
        ans = [""]
        for lst in temp:
            for i in range(len(ans)):
                # print(ans[i])
                for ele in lst:
                    ans.append(ans[i]+ele)
        
        if len(ans) == 1: return []
        return [x for x in ans if len(x) == len(temp)]