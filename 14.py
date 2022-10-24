class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        min_strs = min([len(x) for x in strs])
        if min_strs == 0:
            return ""
        run_word = strs[0]
        for i in range(min_strs):
            for ele in strs:
                if run_word[i] != ele[i]:
                    return run_word[:i]
        return run_word[:min_strs]
            
            