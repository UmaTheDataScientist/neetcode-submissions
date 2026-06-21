class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            # Counted all the characters of the string
            count_s = {}
            count_t = {}
            for ch in s:
                if ch in count_s:
                    count_s[ch]+=1
                else:
                    count_s[ch]=1
            for ch in t:
                if ch in count_t:
                    count_t[ch]+=1
                else:
                    count_t[ch]=1
            for key in count_s:
                if key in count_t:
                    if count_s[key]!=count_t[key]:
                        return False
                else:
                    return False
            return True

        else:
            return False
        