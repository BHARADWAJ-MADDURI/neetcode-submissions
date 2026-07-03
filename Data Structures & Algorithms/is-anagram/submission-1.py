class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hshstr1 = {}
        hshstr2 = {}

        for i in s:
            if i not in hshstr1:
                hshstr1[i] = 1
            else:
                hshstr1[i] += 1
        
        for i in t:
            if i not in hshstr2:
                hshstr2[i] = 1
            else:
                hshstr2[i] += 1
        
        for c in hshstr1:
            if hshstr1[c] != hshstr2.get(c,0):
                return False
        
        return True
        