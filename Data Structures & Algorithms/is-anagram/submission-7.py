class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            seen_s = {}
            seen_t = {}
            for char in s:
                if char in seen_s:
                    seen_s[char] += 1
                else:
                    seen_s[char] = 1
            for char in t:
                if char in seen_t:
                    seen_t[char]+=1
                else:
                    seen_t[char] = 1
            for key in seen_s:
                if key in seen_t:
                    if seen_s[key] != seen_t[key]:
                        return False
                else:
                    return False
            return True
            