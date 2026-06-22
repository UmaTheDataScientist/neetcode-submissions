class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ''
        for word in strs:
            final_string += str(len(word))+'#'+word
        return final_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i=0
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            length_of_string = int(s[i:j])
            start = j+1
            end = start+length_of_string
            decoded_list.append(s[start:end])
            i = end
        return decoded_list
