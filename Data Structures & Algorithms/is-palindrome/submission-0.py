class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_no_alpha = ''
        rev_no_alpha = ''
        i = 0
        while i<len(s):
            if s[i].isalnum():
                s_no_alpha += s[i]
                i+=1
            else:
                i+=1
        for i in range(0,len(s_no_alpha)):
            rev_no_alpha+=s_no_alpha[len(s_no_alpha)-1-i]
        if s_no_alpha.lower() == rev_no_alpha.lower():
            return True
        else:
            return False

            