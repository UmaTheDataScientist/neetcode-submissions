class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        final_list = []
        for ind_str in strs:
            sorted_joined_string = ''.join(sorted(ind_str))
            if sorted_joined_string in seen:
                seen[sorted_joined_string].append(ind_str)
            else:
                seen[sorted_joined_string] = [ind_str]
        for key in seen:
            final_list.append(seen[key])

        return final_list

            