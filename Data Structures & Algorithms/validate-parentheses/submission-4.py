class Solution:
    def isValid(self, s: str) -> bool:
        last_opened = []
        i = 0
        if(len(s)%2!=0):
            return False
        while i in range(0,len(s)):
            if s[i] == '[':
                last_opened.append(']')
            elif s[i] == '{':
                last_opened.append('}')
            elif s[i] == '(':
                last_opened.append(')')
            elif s[i] == ')' and len(last_opened)>0:
                if last_opened[-1] == ')':
                    last_opened.pop()
                else:
                    return False
            elif s[i] == '}' and len(last_opened)>0:
                if last_opened[-1] == '}':
                    last_opened.pop()
                else:
                    return False
            elif s[i] == ']' and len(last_opened)>0:
                if last_opened[-1] == ']':
                    last_opened.pop()
                else:
                    return False
            else:
                return False
            i+=1
        if len(last_opened) == 0:
            return True
        else:
            return False

      

