class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        group_anagrams = []
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word in seen:
                seen[sorted_word].append(strs[i])
            else:
                seen[sorted_word] = [strs[i]]
        for key in seen:
            group_anagrams.append(seen[key])
        return group_anagrams


