class Solution:
    def __init__(self, strs):
        self.strs = strs
    def longestCommonPrefix(self, strs):
        str1 = []
        for i in range(len(strs)):
            newStr = strs[i]
            str1.append(i)
            print(str1)
            #for j in newStr:
                
                
        

                           
strs = ["flower","flight","flow","flood"]
sol1 = Solution(strs)
sol1.longestCommonPrefix(strs)
