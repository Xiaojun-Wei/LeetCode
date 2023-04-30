#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # max_num记录最大连续数, count计算当前连续数
        max_num, counter = 0, 0
        for i in nums:
            # 如果遇到1, counter + 1
            if i == 1:
                counter += 1
            # 如果遇到0, 判断是否更新max_num
            elif i == 0:
                max_num = counter if counter > max_num else max_num
                counter = 0

        # 考虑元素可能全部是0或者全部是1的情况
        max_num = counter if counter > max_num else max_num
        return max_num
