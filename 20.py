class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = "([{"
        cl = ")]}"
        for ele in s:
            if ele in op:
                stack.append(ele)
            else:
                if len(stack)<1:
                    return False
                else:
                    pick = stack.pop()
                    if op.index(pick) != cl.index(ele):
                        return False
        return not len(stack)