class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s = "".join(sorted(s))
            t = "".join(sorted(t))
            for x in range(0,len(s)):
                if s[x]!=t[x]:
                    return False
            return True