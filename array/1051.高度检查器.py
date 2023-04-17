#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights):
        # heights = [1,1,4,2,1,3]
        differ = 0
        heights_num = [0]*max(heights) # use max() here, not len()
        heights_sorted = list()
        for height in heights:
            heights_num[height-1] += 1 
        # heights_num = [3, 1, 1, 1]
        
        for i in range(len(heights_num)):
            heights_sorted += [i+1] * heights_num[i]
        # heights_sorted = [1, 1, 1, 2, 3, 4]
        
        for j in range(len(heights_sorted)):
            if heights_sorted[j] != heights[j]:
                differ += 1

        return differ