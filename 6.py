class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if 0<numRows < 2:
            return s
        else:
            ans = ["" for i in range(numRows)]
            run=0
            c=-1
            for ele in s:
                ans[run]+=ele
                if run == 0 or run == numRows-1:
                    c*=-1
                run+=c
        return "".join(ans)