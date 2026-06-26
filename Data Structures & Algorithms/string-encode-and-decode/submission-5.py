class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ''
        for i in range(len(strs)):
            count_word = len(strs[i])
            final_string+=str(count_word)+'#'+strs[i]
        return final_string


    def decode(self, s: str) -> List[str]:
        flist = []
        i = 0
        j = i
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            length_of_string = int(s[i:j])
            i = j + 1 #start
            end = i + length_of_string
            word = s[i:end]
            flist.append(word)
            i = end
        return flist



            
            


