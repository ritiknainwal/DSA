class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        n = len(strs)

        prefix = strs[0]

        for i in range(1,n):
            
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]


                if prefix == "":
                    return ""
            
        return prefix 
        