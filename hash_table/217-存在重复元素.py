# May 24, 2023

"""
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

示例 1：
输入：nums = [1,2,3,1]
输出：true

示例 2：
输入：nums = [1,2,3,4]
输出：false

示例 3：
输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true
"""

"""
思路：用set可以去重，若有重复元素，则去重后，列表长度必然小于原列表长度，故判断二者长度是否一致即可
"""

"""
时间复杂度：O(n)，n为数组的长度
空间复杂度：O(n)，n为数组的长度
"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# 或者

class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
