class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for single_word in strs:
            key = tuple(sorted(single_word))
            if key not in sorted_dict:
                sorted_dict[key] = [single_word]
            else:
                sorted_dict[key].append(single_word)
        return list(sorted_dict.values())
        
                    


