class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        analist = []
        for i in range(len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            if sorted_word in ana:
                ana[sorted_word].append(strs[i])
            else:
                ana[sorted_word] = [strs[i]]
        for key in ana:
            analist.append(ana[key])
        return analist

