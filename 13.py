class Solution:
    def romanToInt(self, s) -> int:
        romandict = {
            "I"   :   1,
            "IV"  :   4,
            "V"   :   5,
            "IX"  :   9,
            "X"   :   10,
            "XL"  :   40,
            "L"   :   50,
            "XC"  :   90,
            "C"   :   100,
            "CD"  :   400,
            "D"   :   500,
            "CM"  :   900,
            "M"   :   1000,
        }
        temp_s = [x for x in s]
        ans = 0
        while temp_s:
            a = temp_s.pop(0)
            if a in ("I","X","C") and len(temp_s)>0:
                b = temp_s[0]
                if romandict[b] > romandict[a]:
                    ans += romandict[a+b]
                    temp_s.pop(0)
                else:
                    ans += romandict[a]
            else:
                ans += romandict[a]
            
        return ans