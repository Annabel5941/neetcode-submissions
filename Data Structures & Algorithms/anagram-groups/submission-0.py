class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ['']*len(strs)

        for i in range(len(strs)):
            sorted_strs[i] = ''.join(sorted(list(strs[i])))

        str_dict = {}
        for key, value in zip(sorted_strs, strs):
            str_dict.setdefault(key, []).append(value)

        #print output using dict
        return [str_dict[key] for key in str_dict]
        