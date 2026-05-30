class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if "" in strs:
            return ""
        common_prefix = ""

        try:
            for index in range(len(strs[0])):
                common_prefix += strs[0][index]
                print(common_prefix)
                for string in strs:
                    if common_prefix not in string:
                        return common_prefix[:-1]
            return common_prefix

        except IndexError:
            return common_prefix